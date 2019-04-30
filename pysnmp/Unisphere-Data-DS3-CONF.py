#
# PySNMP MIB module Unisphere-Data-DS3-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-DS3-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
dsx3FarEndConfigEntry, dsx3TotalEntry, dsx3FarEndCurrentEntry, dsx3SendCode, dsx3IntervalEntry, dsx3CurrentEntry, dsx3ConfigEntry, dsx3FracEntry, dsx3FarEndTotalEntry, dsx3FarEndIntervalEntry = mibBuilder.importSymbols("RFC1407-MIB", "dsx3FarEndConfigEntry", "dsx3TotalEntry", "dsx3FarEndCurrentEntry", "dsx3SendCode", "dsx3IntervalEntry", "dsx3CurrentEntry", "dsx3ConfigEntry", "dsx3FracEntry", "dsx3FarEndTotalEntry", "dsx3FarEndIntervalEntry")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, ObjectIdentity, Gauge32, Counter32, Unsigned32, IpAddress, Bits, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Gauge32", "Counter32", "Unsigned32", "IpAddress", "Bits", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "TimeTicks", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdDs3Group2, usdDs3Group, usdDs3Group4, usdDs3FarEndGroup, usdDs3Group5, usdDs3Group3 = mibBuilder.importSymbols("Unisphere-Data-DS3-MIB", "usdDs3Group2", "usdDs3Group", "usdDs3Group4", "usdDs3FarEndGroup", "usdDs3Group5", "usdDs3Group3")
usdDs3Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11))
usdDs3Agent.setRevisions(('2002-08-27 18:48', '2001-04-18 19:41',))
if mibBuilder.loadTexts: usdDs3Agent.setLastUpdated('200208271848Z')
if mibBuilder.loadTexts: usdDs3Agent.setOrganization('Unisphere Networks, Inc.')
usdDs3AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV1 = usdDs3AgentV1.setProductRelease('Version 1 of the DS3 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS3 component was supported in the Unisphere\n        RX 1.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV1 = usdDs3AgentV1.setStatus('obsolete')
usdDs3AgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV2 = usdDs3AgentV2.setProductRelease('Version 2 of the DS3 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS3 component was supported in the Unisphere\n        RX 1.1 thru RX 2.5 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV2 = usdDs3AgentV2.setStatus('obsolete')
usdDs3AgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV3 = usdDs3AgentV3.setProductRelease('Version 3 of the DS3 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS3 component was supported in the Unisphere\n        RX 2.6 thru RX 2.9 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV3 = usdDs3AgentV3.setStatus('obsolete')
usdDs3AgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV4 = usdDs3AgentV4.setProductRelease('Version 4 of the DS3 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS3 component was supported in the Unisphere\n        RX 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV4 = usdDs3AgentV4.setStatus('obsolete')
usdDs3AgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV5 = usdDs3AgentV5.setProductRelease('Version 5 of the DS3 component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DS3 component is supported in the Unisphere\n        RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3AgentV5 = usdDs3AgentV5.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-DS3-CONF", PYSNMP_MODULE_ID=usdDs3Agent, usdDs3AgentV4=usdDs3AgentV4, usdDs3AgentV3=usdDs3AgentV3, usdDs3Agent=usdDs3Agent, usdDs3AgentV2=usdDs3AgentV2, usdDs3AgentV5=usdDs3AgentV5, usdDs3AgentV1=usdDs3AgentV1)
