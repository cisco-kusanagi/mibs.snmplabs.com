#
# PySNMP MIB module CISCO-IF-EXTENSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IF-EXTENSION-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
IpAddress, ModuleIdentity, TimeTicks, Counter32, Counter64, Gauge32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ObjectIdentity, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "TimeTicks", "Counter32", "Counter64", "Gauge32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ObjectIdentity", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIfExtensionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 395))
ciscoIfExtensionCapability.setRevisions(('2015-06-03 00:00', '2013-09-05 00:00', '2012-03-01 00:00', '2011-03-21 00:00', '2008-03-24 00:00', '2007-11-05 00:00', '2007-08-30 00:00', '2007-04-19 00:00', '2006-02-21 00:00', '2005-04-14 00:00', '2005-03-04 00:00', '2004-01-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIfExtensionCapability.setRevisionsDescriptions(('Added ciscoIfExtensionTableIntfGroup3SupR02 and VARIATIONs for cieIfTransceiverFrequencyConfig, cieIfFillPatternConfig, cieIfIgnoreBitErrorsConfig and cieIfIgnoreInterruptThresholdConfig in capability statement ciscoIfExtCapNxOSV06R0201PMDS9000 and ciscoIfExtCapNxOSV06R0202PN7K.', 'Added agent capability statement ciscoIfExtCapNxOSV06R0201PMDS9000 and ciscoIfExtCapNxOSV06R0202PN7K.', 'Added ciscoIfExtCapV15R0002SGPCat4K agent capability statement.', 'Added ciscoIfExtCapNXOSV52R1MDS9000 agent capability statement.', 'Added ciscoIfExtCapCatOSV08R0701PCat6K agent capability statement.', 'Added ciscoIfExtCapc4710aceVA1R700 agent capabilities for ACE 4710 Application Control Engine Appliance.', 'Added ciscoIfExtCapV12R0233SXHPCat6K capability statement.', 'Added ciscoIfExtCapV12R0229SM1 and ciscoIfExtCapV12R0412MR1 capability statements.', 'Added capability statement ciscoIfExtCapabilityACSWV03R000 for Application Control Engine (ACE).', 'Added capability statement ciscoIfExtCapSanOSV30R1MDS9000.', 'Added capability statement ciscoIfExtCapV12R0217bSXAPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIfExtensionCapability.setLastUpdated('201506030000Z')
if mibBuilder.loadTexts: ciscoIfExtensionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIfExtensionCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIfExtensionCapability.setDescription('The capabilities description of CISCO-IF-EXTENSION-MIB.')
ciscoIfExtensionCapV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionCapV08R0301 = ciscoIfExtensionCapV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionCapV08R0301 = ciscoIfExtensionCapV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtensionCapV08R0301.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapV12R0217bSXAPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0217bSXAPCat6K = ciscoIfExtCapV12R0217bSXAPCat6K.setProductRelease('Cisco IOS 12.2(17b)SXA on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0217bSXAPCat6K = ciscoIfExtCapV12R0217bSXAPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapV12R0217bSXAPCat6K.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapSanOSV30R1MDS9000 = ciscoIfExtCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0 on Cisco MDS 9000\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapSanOSV30R1MDS9000 = ciscoIfExtCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapSanOSV30R1MDS9000.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapabilityACSWV03R000 = ciscoIfExtCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapabilityACSWV03R000 = ciscoIfExtCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapabilityACSWV03R000.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapV12R0229SM1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0229SM1 = ciscoIfExtCapV12R0229SM1.setProductRelease('Cisco IOS 12.2(29)SM1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0229SM1 = ciscoIfExtCapV12R0229SM1.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapV12R0229SM1.setDescription('IOS 12.2(29)SM1 Cisco CISCO-IF-EXTENSION-MIB User Agent MIB capabilities.')
ciscoIfExtCapV12R0412MR1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0412MR1 = ciscoIfExtCapV12R0412MR1.setProductRelease('Cisco IOS 12.4(2)MR1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0412MR1 = ciscoIfExtCapV12R0412MR1.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapV12R0412MR1.setDescription('IOS 12.4(2)MR1 Cisco CISCO-IF-EXTENSION-MIB User Agent MIB capabilities.')
ciscoIfExtCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0233SXHPCat6K = ciscoIfExtCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0233SXHPCat6K = ciscoIfExtCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapV12R0233SXHPCat6K.setDescription('CISCO-IF-EXTENSION-MIB agent capabilities.')
ciscoIfExtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapc4710aceVA1R700 = ciscoIfExtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapc4710aceVA1R700 = ciscoIfExtCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapc4710aceVA1R700.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapCatOSV08R0701PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapCatOSV08R0701PCat6K = ciscoIfExtCapCatOSV08R0701PCat6K.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500 and\n                     Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapCatOSV08R0701PCat6K = ciscoIfExtCapCatOSV08R0701PCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapCatOSV08R0701PCat6K.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapNXOSV52R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNXOSV52R1MDS9000 = ciscoIfExtCapNXOSV52R1MDS9000.setProductRelease('Cisco NXOS 5.2(1) on MDS 9000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNXOSV52R1MDS9000 = ciscoIfExtCapNXOSV52R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapNXOSV52R1MDS9000.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV15R0002SGPCat4K = ciscoIfExtCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Catalyst 4000 family\n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV15R0002SGPCat4K = ciscoIfExtCapV15R0002SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapV15R0002SGPCat4K.setDescription('CISCO-IF-EXTENSION-MIB agent capabilities.')
ciscoIfExtCapNxOSV06R0201PMDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0201PMDS9000 = ciscoIfExtCapNxOSV06R0201PMDS9000.setProductRelease('Cisco NX-OS 6.2(1) on MDS 9000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0201PMDS9000 = ciscoIfExtCapNxOSV06R0201PMDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapNxOSV06R0201PMDS9000.setDescription('CISCO-IF-EXTENSION-MIB agent capabilities.')
ciscoIfExtCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0202PN7K = ciscoIfExtCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0202PN7K = ciscoIfExtCapNxOSV06R0202PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapNxOSV06R0202PN7K.setDescription('CISCO-IF-EXTENSION-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-IF-EXTENSION-CAPABILITY", ciscoIfExtCapV15R0002SGPCat4K=ciscoIfExtCapV15R0002SGPCat4K, ciscoIfExtCapNXOSV52R1MDS9000=ciscoIfExtCapNXOSV52R1MDS9000, ciscoIfExtensionCapV08R0301=ciscoIfExtensionCapV08R0301, ciscoIfExtensionCapability=ciscoIfExtensionCapability, ciscoIfExtCapV12R0233SXHPCat6K=ciscoIfExtCapV12R0233SXHPCat6K, PYSNMP_MODULE_ID=ciscoIfExtensionCapability, ciscoIfExtCapc4710aceVA1R700=ciscoIfExtCapc4710aceVA1R700, ciscoIfExtCapabilityACSWV03R000=ciscoIfExtCapabilityACSWV03R000, ciscoIfExtCapNxOSV06R0201PMDS9000=ciscoIfExtCapNxOSV06R0201PMDS9000, ciscoIfExtCapSanOSV30R1MDS9000=ciscoIfExtCapSanOSV30R1MDS9000, ciscoIfExtCapV12R0229SM1=ciscoIfExtCapV12R0229SM1, ciscoIfExtCapV12R0412MR1=ciscoIfExtCapV12R0412MR1, ciscoIfExtCapV12R0217bSXAPCat6K=ciscoIfExtCapV12R0217bSXAPCat6K, ciscoIfExtCapCatOSV08R0701PCat6K=ciscoIfExtCapCatOSV08R0701PCat6K, ciscoIfExtCapNxOSV06R0202PN7K=ciscoIfExtCapNxOSV06R0202PN7K)
