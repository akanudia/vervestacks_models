"""
Complete AR6 System Test
Tests the full AR6 scenario generation + README integration workflow
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from create_ar6_r10_scenario import create_ar6_r10_scenario
from update_readme_with_ar6 import update_readme_with_ar6_scenarios
from .readme_generator import ReadmeGenerator


def test_complete_ar6_workflow(iso_code):
    """Test the complete AR6 workflow: Excel generation + README integration"""
    
    print(f"\n🚀 Testing Complete AR6 Workflow for {iso_code}")
    print("=" * 60)
    
    try:
        # Step 1: Create AR6 scenario Excel file
        print("📊 Step 1: Creating AR6 scenario Excel file...")
        scenario_stats = create_ar6_r10_scenario(iso_code)
        
        if scenario_stats:
            print(f"   ✅ Excel file created successfully")
            print(f"   🌍 Region: {scenario_stats['r10_region']}")
            print(f"   📈 AR6 records: {scenario_stats['ar6_records']}")
            print(f"   📊 IEA records: {scenario_stats['iea_records']}")
            
            # Step 2: Generate AR6 insights for README
            print("\n📝 Step 2: Generating AR6 insights for README...")
            
            # Load the AR6 data we just created
            import pandas as pd
            ar6_data = pd.read_csv('ar6_r10_scenario_drivers.csv')
            ar6_region_data = ar6_data[ar6_data['Region'] == scenario_stats['r10_region']]
            
            # Generate insights
            readme_gen = ReadmeGenerator()
            ar6_insights = readme_gen.calculate_ar6_insights(
                scenario_stats['r10_region'], 
                ar6_region_data, 
                iso_code
            )
            
            print(f"   ✅ Generated insights for {scenario_stats['r10_region']}")
            print(f"   💰 CO2 2030 C1: ${ar6_insights.get('co2_2030_c1_median', 0):.0f}/tCO2")
            print(f"   💰 CO2 2030 C7: ${ar6_insights.get('co2_2030_c7_median', 0):.0f}/tCO2")
            print(f"   ⚡ Elec growth C1: {ar6_insights.get('elec_growth_2050_c1', 0):.1f}x by 2050")
            print(f"   🚗 Transport elec: {ar6_insights.get('transport_2050_c1_median', 0):.1f}% by 2050")
            
            # Step 3: Generate README content (test only - don't update actual README)
            print("\n📚 Step 3: Generating README content...")
            
            readme_content = readme_gen.generate_readme_content(
                iso_code,
                processing_params=ar6_insights,
                ar6_scenarios=True
            )
            
            # Save test README
            test_readme_file = f'test_ar6_readme_{iso_code}.md'
            with open(test_readme_file, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            
            print(f"   ✅ Generated README content: {len(readme_content)} characters")
            print(f"   📄 Saved test README: {test_readme_file}")
            
            # Step 4: Show key insights
            print(f"\n🎯 Step 4: Key AR6 Insights for {iso_code} ({scenario_stats['r10_region']}):")
            print(f"   🌡️  Climate Categories: {', '.join(scenario_stats['scenario_categories'])}")
            print(f"   📅 Time Coverage: {min(scenario_stats['years_covered'])}-{max(scenario_stats['years_covered'])}")
            print(f"   📊 Data Attributes: {len(scenario_stats['scenario_attributes'])} types")
            print(f"   🔬 Model Consensus: {ar6_insights.get('model_agreement_level', 'Unknown')}")
            print(f"   🌍 Regional Pattern: {ar6_insights.get('regional_convergence_pattern', 'Unknown')}")
            
            return True
            
        else:
            print("   ❌ Failed to create AR6 scenario file")
            return False
            
    except Exception as e:
        print(f"❌ Error in complete AR6 workflow: {e}")
        return False


def main():
    """Test the complete AR6 system with multiple countries"""
    
    print("🧪 AR6 Complete System Test")
    print("Testing Excel generation + README integration")
    
    # Test countries from different R10 regions
    test_countries = [
        ('CHE', 'R10EUROPE'),
        ('USA', 'R10NORTH_AM'),
        ('JPN', 'R10PAC_OECD')
    ]
    
    results = {}
    
    for iso_code, expected_region in test_countries:
        success = test_complete_ar6_workflow(iso_code)
        results[iso_code] = success
        print("-" * 60)
    
    # Summary
    print(f"\n📋 Test Results Summary:")
    for iso_code, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {iso_code}: {status}")
    
    total_passed = sum(results.values())
    print(f"\n🎯 Overall: {total_passed}/{len(results)} tests passed")
    
    if total_passed == len(results):
        print("🎉 All AR6 system tests completed successfully!")
    else:
        print("⚠️  Some tests failed - check logs above")


if __name__ == "__main__":
    main()
