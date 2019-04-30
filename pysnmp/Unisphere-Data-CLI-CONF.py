#
# PySNMP MIB module Unisphere-Data-CLI-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-CLI-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Gauge32, Integer32, Bits, NotificationType, MibIdentifier, iso, Unsigned32, ObjectIdentity, ModuleIdentity, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Bits", "NotificationType", "MibIdentifier", "iso", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdCliSecurityAlertGroup, usdCliSecurityTrapGroup, usdCliGroup = mibBuilder.importSymbols("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertGroup", "usdCliSecurityTrapGroup", "usdCliGroup")
usdCliAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 6))
usdCliAgent.setRevisions(('2001-03-27 22:30',))
if mibBuilder.loadTexts: usdCliAgent.setLastUpdated('200103272230Z')
if mibBuilder.loadTexts: usdCliAgent.setOrganization('Unisphere Networks, Inc.')
usdCliAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliAgentV1 = usdCliAgentV1.setProductRelease('Version 1 of the CLI Security Management component of the Unisphere\n        Routing Switch SNMP agent.  This version of the CLI Security Management\n        component is supported in the Unisphere RX 1.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliAgentV1 = usdCliAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-CLI-CONF", usdCliAgentV1=usdCliAgentV1, usdCliAgent=usdCliAgent, PYSNMP_MODULE_ID=usdCliAgent)
