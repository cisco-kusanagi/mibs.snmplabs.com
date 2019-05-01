#
# PySNMP MIB module CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:14:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Integer32, Counter32, MibIdentifier, iso, Gauge32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, ModuleIdentity, TimeTicks, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibIdentifier", "iso", "Gauge32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "ModuleIdentity", "TimeTicks", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoThreatMitigationServiceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 532))
ciscoThreatMitigationServiceCapability.setRevisions(('2007-05-17 00:00', '2007-01-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setRevisionsDescriptions(('Added the agent capabilities statement for ciscoTmsCapIOSV12R05T.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setLastUpdated('200705170000Z')
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-tms@cisco.com')
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setDescription('Agent capabilities for CISCO-THREAT-MITIGATION-SERVICE-MIB.')
ciscoTmsCapIOSV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 532, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R02S = ciscoTmsCapIOSV12R02S.setProductRelease('Cisco IOS 12.2S ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R02S = ciscoTmsCapIOSV12R02S.setStatus('current')
if mibBuilder.loadTexts: ciscoTmsCapIOSV12R02S.setDescription('CISCO-THREAT-MITIGATION-SERVICE-MIB capabilities.')
ciscoTmsCapIOSV12R05T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 532, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R05T = ciscoTmsCapIOSV12R05T.setProductRelease('Cisco IOS 12.5T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R05T = ciscoTmsCapIOSV12R05T.setStatus('current')
if mibBuilder.loadTexts: ciscoTmsCapIOSV12R05T.setDescription('CISCO-THREAT-MITIGATION-SERVICE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY", ciscoTmsCapIOSV12R05T=ciscoTmsCapIOSV12R05T, PYSNMP_MODULE_ID=ciscoThreatMitigationServiceCapability, ciscoThreatMitigationServiceCapability=ciscoThreatMitigationServiceCapability, ciscoTmsCapIOSV12R02S=ciscoTmsCapIOSV12R02S)
