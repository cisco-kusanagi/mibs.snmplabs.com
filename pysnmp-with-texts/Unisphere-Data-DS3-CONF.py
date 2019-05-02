#
# PySNMP MIB module Unisphere-Data-DS3-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-DS3-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:30:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dsx3FarEndTotalEntry, dsx3SendCode, dsx3TotalEntry, dsx3FarEndCurrentEntry, dsx3FarEndIntervalEntry, dsx3ConfigEntry, dsx3CurrentEntry, dsx3IntervalEntry, dsx3FarEndConfigEntry, dsx3FracEntry = mibBuilder.importSymbols("RFC1407-MIB", "dsx3FarEndTotalEntry", "dsx3SendCode", "dsx3TotalEntry", "dsx3FarEndCurrentEntry", "dsx3FarEndIntervalEntry", "dsx3ConfigEntry", "dsx3CurrentEntry", "dsx3IntervalEntry", "dsx3FarEndConfigEntry", "dsx3FracEntry")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Gauge32, Integer32, iso, ModuleIdentity, Unsigned32, Bits, Counter32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "iso", "ModuleIdentity", "Unsigned32", "Bits", "Counter32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "MibIdentifier", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdDs3Group, usdDs3Group3, usdDs3Group2, usdDs3FarEndGroup, usdDs3Group4, usdDs3Group5 = mibBuilder.importSymbols("Unisphere-Data-DS3-MIB", "usdDs3Group", "usdDs3Group3", "usdDs3Group2", "usdDs3FarEndGroup", "usdDs3Group4", "usdDs3Group5")
usdDs3Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11))
usdDs3Agent.setRevisions(('2002-08-27 18:48', '2001-04-18 19:41',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdDs3Agent.setRevisionsDescriptions(('Added far end support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdDs3Agent.setLastUpdated('200208271848Z')
if mibBuilder.loadTexts: usdDs3Agent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdDs3Agent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdDs3Agent.setDescription('The agent capabilities definitions for the DS3 component of the SNMP agent in the Unisphere Data Routing Switch family of products.')
usdDs3AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV1 = usdDs3AgentV1.setProductRelease('Version 1 of the DS3 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS3 component was supported in the Unisphere\n        RX 1.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV1 = usdDs3AgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdDs3AgentV1.setDescription('The MIBs supported by the SNMP agent for the DS3 application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for line type and cell scrambler objects.')
usdDs3AgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV2 = usdDs3AgentV2.setProductRelease('Version 2 of the DS3 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS3 component was supported in the Unisphere\n        RX 1.1 thru RX 2.5 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV2 = usdDs3AgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdDs3AgentV2.setDescription('The MIBs supported by the SNMP agent for the DS3 application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for DSU configuration objects.')
usdDs3AgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV3 = usdDs3AgentV3.setProductRelease('Version 3 of the DS3 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS3 component was supported in the Unisphere\n        RX 2.6 thru RX 2.9 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV3 = usdDs3AgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: usdDs3AgentV3.setDescription('The MIBs supported by the SNMP agent for the DS3 application in the Unisphere Routing Switch. These capabilities became obsolete when support was added for dynamic DS3 interface objects.')
usdDs3AgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV4 = usdDs3AgentV4.setProductRelease('Version 4 of the DS3 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS3 component was supported in the Unisphere\n        RX 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV4 = usdDs3AgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: usdDs3AgentV4.setDescription('The MIBs supported by the SNMP agent for the DS3 application in the Unisphere Routing Switch. These capabilities became obsolete when far end support')
usdDs3AgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV5 = usdDs3AgentV5.setProductRelease('Version 5 of the DS3 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS3 component is supported in the Unisphere\n        RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV5 = usdDs3AgentV5.setStatus('current')
if mibBuilder.loadTexts: usdDs3AgentV5.setDescription('The MIBs supported by the SNMP agent for the DS3 application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-DS3-CONF", usdDs3AgentV4=usdDs3AgentV4, usdDs3AgentV3=usdDs3AgentV3, usdDs3AgentV1=usdDs3AgentV1, PYSNMP_MODULE_ID=usdDs3Agent, usdDs3Agent=usdDs3Agent, usdDs3AgentV2=usdDs3AgentV2, usdDs3AgentV5=usdDs3AgentV5)
