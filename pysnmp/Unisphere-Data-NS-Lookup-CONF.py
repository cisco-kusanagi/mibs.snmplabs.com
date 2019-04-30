#
# PySNMP MIB module Unisphere-Data-NS-Lookup-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-NS-Lookup-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
lookupGroup, = mibBuilder.importSymbols("DISMAN-NSLOOKUP-MIB", "lookupGroup")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Gauge32, Unsigned32, ObjectIdentity, IpAddress, ModuleIdentity, TimeTicks, MibIdentifier, Bits, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Bits", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdNsLookupAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 27))
usdNsLookupAgent.setRevisions(('2001-03-28 22:22',))
if mibBuilder.loadTexts: usdNsLookupAgent.setLastUpdated('200103282222Z')
if mibBuilder.loadTexts: usdNsLookupAgent.setOrganization('Unisphere Networks, Inc.')
usdNsLookupAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 27, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdNsLookupAgentV1 = usdNsLookupAgentV1.setProductRelease('Version 1 of the NS Lookup component of the Unisphere Routing Switch\n        SNMP agent.  This version of the NS Lookup component is supported in\n        the Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdNsLookupAgentV1 = usdNsLookupAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-NS-Lookup-CONF", PYSNMP_MODULE_ID=usdNsLookupAgent, usdNsLookupAgent=usdNsLookupAgent, usdNsLookupAgentV1=usdNsLookupAgentV1)
