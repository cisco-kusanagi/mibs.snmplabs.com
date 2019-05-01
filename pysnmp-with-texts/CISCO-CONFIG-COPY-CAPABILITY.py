#
# PySNMP MIB module CISCO-CONFIG-COPY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CONFIG-COPY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:53:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ConfigFileType, ConfigCopyProtocol, ConfigCopyFailCause, ConfigCopyState = mibBuilder.importSymbols("CISCO-CONFIG-COPY-MIB", "ConfigFileType", "ConfigCopyProtocol", "ConfigCopyFailCause", "ConfigCopyState")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, MibIdentifier, Integer32, Bits, ObjectIdentity, IpAddress, Counter64, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Integer32", "Bits", "ObjectIdentity", "IpAddress", "Counter64", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "iso", "TimeTicks")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoConfigCopyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 128))
ciscoConfigCopyCapability.setRevisions(('2006-02-08 00:00', '2005-05-24 00:00', '2004-06-08 00:00', '2004-03-17 00:00', '2002-04-29 00:00', '2000-09-06 00:00', '1999-10-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoConfigCopyCapability.setRevisionsDescriptions(('Added Agent Capability statement ciscoConfigCopyCapIOSXRV2R0CRS1.', 'Added capability statement ciscoConfigCopyCapMDS3R0.', 'Added capability statement ciscoConfigCopyCapCatOSV08R0401.', 'Adding new varbind for ccCopyCompletion Notification.', 'Added ciscoConfigCopyCapabilityV2R0175 for RPM-PR module in MGX8850.', 'Added VARIATION clauses to ccCopySourceFileType and ccCopyDestFileType.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoConfigCopyCapability.setLastUpdated('200602080000Z')
if mibBuilder.loadTexts: ciscoConfigCopyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoConfigCopyCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoConfigCopyCapability.setDescription('This is the Agent Capabilities for CISCO-CONFIG-COPY-MIB.')
ciscoConfigCopyCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R00 = ciscoConfigCopyCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R00 = ciscoConfigCopyCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapabilityV12R00.setDescription('CONFIG-COPY MIB capabilities')
ciscoConfigCopyCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R01 = ciscoConfigCopyCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R01 = ciscoConfigCopyCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapabilityV12R01.setDescription('CONFIG-COPY MIB capabilities')
ciscoConfigCopyCapabilityV2R0175 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV2R0175 = ciscoConfigCopyCapabilityV2R0175.setProductRelease('MGX8850 Release 2.1.75')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV2R0175 = ciscoConfigCopyCapabilityV2R0175.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapabilityV2R0175.setDescription('CISCO-CONFIG-COPY-MIB Capabilities for RPM-PR(Router Module).')
ciscoConfigCopyCapabilityV12R30S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R30S = ciscoConfigCopyCapabilityV12R30S.setProductRelease('Cisco IOS 12.30S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R30S = ciscoConfigCopyCapabilityV12R30S.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapabilityV12R30S.setDescription('CONFIG-COPY MIB capabilities')
ciscoConfigCopyCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapCatOSV08R0401 = ciscoConfigCopyCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapCatOSV08R0401 = ciscoConfigCopyCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapCatOSV08R0401.setDescription('CISCO-CONFIG-COPY-MIB capabilities.')
ciscoConfigCopyCapMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapMDS3R0 = ciscoConfigCopyCapMDS3R0.setProductRelease('Cisco MDS 3.0(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapMDS3R0 = ciscoConfigCopyCapMDS3R0.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapMDS3R0.setDescription('CISCO-CONFIG-COPY-MIB capabilities.')
ciscoConfigCopyCapIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapIOSXRV2R0CRS1 = ciscoConfigCopyCapIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapIOSXRV2R0CRS1 = ciscoConfigCopyCapIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapIOSXRV2R0CRS1.setDescription('CISCO-CONFIG-COPY-MIB Capabilities for IOS XR release 2.0')
mibBuilder.exportSymbols("CISCO-CONFIG-COPY-CAPABILITY", ciscoConfigCopyCapMDS3R0=ciscoConfigCopyCapMDS3R0, ciscoConfigCopyCapabilityV12R30S=ciscoConfigCopyCapabilityV12R30S, ciscoConfigCopyCapabilityV12R00=ciscoConfigCopyCapabilityV12R00, ciscoConfigCopyCapabilityV2R0175=ciscoConfigCopyCapabilityV2R0175, ciscoConfigCopyCapabilityV12R01=ciscoConfigCopyCapabilityV12R01, ciscoConfigCopyCapability=ciscoConfigCopyCapability, ciscoConfigCopyCapCatOSV08R0401=ciscoConfigCopyCapCatOSV08R0401, ciscoConfigCopyCapIOSXRV2R0CRS1=ciscoConfigCopyCapIOSXRV2R0CRS1, PYSNMP_MODULE_ID=ciscoConfigCopyCapability)
