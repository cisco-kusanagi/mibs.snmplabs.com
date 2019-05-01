#
# PySNMP MIB module Unisphere-Data-DS1-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-DS1-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:30:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
dsx1CurrentEntry, dsx1ConfigEntry, dsx1FarEndTotalEntry, dsx1FracEntry, dsx1TotalEntry, dsx1FarEndIntervalEntry, dsx1FarEndCurrentEntry, dsx1IntervalEntry = mibBuilder.importSymbols("RFC1406-MIB", "dsx1CurrentEntry", "dsx1ConfigEntry", "dsx1FarEndTotalEntry", "dsx1FracEntry", "dsx1TotalEntry", "dsx1FarEndIntervalEntry", "dsx1FarEndCurrentEntry", "dsx1IntervalEntry")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
TimeTicks, Counter32, Integer32, NotificationType, Unsigned32, iso, IpAddress, MibIdentifier, Gauge32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Integer32", "NotificationType", "Unsigned32", "iso", "IpAddress", "MibIdentifier", "Gauge32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdDs1Group2, usdDs1Group3, usdDs1Group, usdDs1Group1 = mibBuilder.importSymbols("Unisphere-Data-DS1-MIB", "usdDs1Group2", "usdDs1Group3", "usdDs1Group", "usdDs1Group1")
usdDs1Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10))
usdDs1Agent.setRevisions(('2002-05-13 16:34', '2001-03-29 20:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdDs1Agent.setRevisionsDescriptions(('Add far end statistics support. More configuration objects were added to Unisphere-Data-DS1-MIB.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdDs1Agent.setLastUpdated('200205131634Z')
if mibBuilder.loadTexts: usdDs1Agent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdDs1Agent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdDs1Agent.setDescription('The agent capabilities definitions for the DS1 component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdDs1AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1AgentV1 = usdDs1AgentV1.setProductRelease('Version 1 of the DS1 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS1 component was supported in the Unisphere\n        RX 1.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1AgentV1 = usdDs1AgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdDs1AgentV1.setDescription('The MIBs supported by the SNMP agent for the DS1 application in the Unisphere Routing Switch. This version became obsolete when new objects were added to the Unisphere-Data-DS1-MIB.')
usdDs1AgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1AgentV2 = usdDs1AgentV2.setProductRelease('Version 2 of the DS1 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS1 component was supported in the Unisphere\n        RX 1.1 thru RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1AgentV2 = usdDs1AgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdDs1AgentV2.setDescription('The MIBs supported by the SNMP agent for the DS1 application in the Unisphere Routing Switch. This version became obsolete when dynamic DS1 interface support was added to the Unisphere-Data-DS1-MIB.')
usdDs1AgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1AgentV3 = usdDs1AgentV3.setProductRelease('Version 3 of the DS1 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS1 component was supported in the Unisphere\n        RX 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1AgentV3 = usdDs1AgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: usdDs1AgentV3.setDescription('The MIBs supported by the SNMP agent for the DS1 application in the Unisphere Routing Switch. This version became obsolete when far end statistics support was added and more configuration objects were added to the Unisphere-Data-DS1-MIB.')
usdDs1AgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1AgentV4 = usdDs1AgentV4.setProductRelease('Version 4 of the DS1 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS1 component is supported in the Unisphere\n        RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1AgentV4 = usdDs1AgentV4.setStatus('current')
if mibBuilder.loadTexts: usdDs1AgentV4.setDescription('The MIBs supported by the SNMP agent for the DS1 application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-DS1-CONF", usdDs1AgentV4=usdDs1AgentV4, usdDs1AgentV3=usdDs1AgentV3, PYSNMP_MODULE_ID=usdDs1Agent, usdDs1AgentV2=usdDs1AgentV2, usdDs1Agent=usdDs1Agent, usdDs1AgentV1=usdDs1AgentV1)
