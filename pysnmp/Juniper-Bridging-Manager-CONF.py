#
# PySNMP MIB module Juniper-Bridging-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Bridging-Manager-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, iso, ObjectIdentity, TimeTicks, Counter64, Bits, NotificationType, Gauge32, MibIdentifier, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "iso", "ObjectIdentity", "TimeTicks", "Counter64", "Bits", "NotificationType", "Gauge32", "MibIdentifier", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniBridgingMgrAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 61))
juniBridgingMgrAgent.setRevisions(('2003-09-26 20:47', '2002-10-02 15:26',))
if mibBuilder.loadTexts: juniBridgingMgrAgent.setLastUpdated('200309262047Z')
if mibBuilder.loadTexts: juniBridgingMgrAgent.setOrganization('Juniper Networks, Inc.')
juniBridgingMgrAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 61, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgingMgrAgentV1 = juniBridgingMgrAgentV1.setProductRelease('Version 1 of the Bridging Manager component of the JUNOSe SNMP agent.\n        This version of the Bridging Manager component is supported in JUNOSe\n        5.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgingMgrAgentV1 = juniBridgingMgrAgentV1.setStatus('current')
mibBuilder.exportSymbols("Juniper-Bridging-Manager-CONF", juniBridgingMgrAgentV1=juniBridgingMgrAgentV1, PYSNMP_MODULE_ID=juniBridgingMgrAgent, juniBridgingMgrAgent=juniBridgingMgrAgent)
