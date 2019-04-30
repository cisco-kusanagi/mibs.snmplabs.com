#
# PySNMP MIB module Unisphere-Data-Log-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Log-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, TimeTicks, Counter32, MibIdentifier, Bits, NotificationType, ObjectIdentity, Integer32, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Counter32", "MibIdentifier", "Bits", "NotificationType", "ObjectIdentity", "Integer32", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdLogGroup, usdLogTrapGroup, usdLogGroup2 = mibBuilder.importSymbols("Unisphere-Data-LOG-MIB", "usdLogGroup", "usdLogTrapGroup", "usdLogGroup2")
usdLogAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26))
usdLogAgent.setRevisions(('2001-03-28 22:07',))
if mibBuilder.loadTexts: usdLogAgent.setLastUpdated('200103282207Z')
if mibBuilder.loadTexts: usdLogAgent.setOrganization('Unisphere Networks, Inc.')
usdLogAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogAgentV1 = usdLogAgentV1.setProductRelease('Version 1 of the logging managment component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Log component was supported in\n        the Unisphere RX 1.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogAgentV1 = usdLogAgentV1.setStatus('obsolete')
usdLogAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogAgentV2 = usdLogAgentV2.setProductRelease('Version 2 of the logging managment component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Log component is supported in\n        the Unisphere RX 2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogAgentV2 = usdLogAgentV2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Log-CONF", PYSNMP_MODULE_ID=usdLogAgent, usdLogAgent=usdLogAgent, usdLogAgentV2=usdLogAgentV2, usdLogAgentV1=usdLogAgentV1)
