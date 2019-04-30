#
# PySNMP MIB module Unisphere-Data-HDLC-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-HDLC-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ObjectIdentity, MibIdentifier, Gauge32, TimeTicks, Integer32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ObjectIdentity", "MibIdentifier", "Gauge32", "TimeTicks", "Integer32", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdHdlcGroup2, usdHdlcGroup3, usdHdlcGroup = mibBuilder.importSymbols("Unisphere-Data-HDLC-MIB", "usdHdlcGroup2", "usdHdlcGroup3", "usdHdlcGroup")
usdHdlcAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18))
usdHdlcAgent.setRevisions(('2001-03-28 14:17',))
if mibBuilder.loadTexts: usdHdlcAgent.setLastUpdated('200103281417Z')
if mibBuilder.loadTexts: usdHdlcAgent.setOrganization('Unisphere Networks, Inc.')
usdHdlcAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV1 = usdHdlcAgentV1.setProductRelease('Version 1 of the HDLC component of the Unisphere Routing Switch SNMP\n        agent.  This version of the HDLC component was supported in the\n        Unisphere RX 1.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV1 = usdHdlcAgentV1.setStatus('obsolete')
usdHdlcAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV2 = usdHdlcAgentV2.setProductRelease('Version 2 of the HDLC component of the Unisphere Routing Switch SNMP\n        agent.  This version of the HDLC component was supported in the\n        Unisphere RX 1.1 thru 3.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV2 = usdHdlcAgentV2.setStatus('current')
usdHdlcAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV3 = usdHdlcAgentV3.setProductRelease('Version 3 of the HDLC component of the Unisphere Routing Switch SNMP\n        agent.  This version of the HDLC component is supported in the Unisphere\n        RX 3.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV3 = usdHdlcAgentV3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-HDLC-CONF", usdHdlcAgentV3=usdHdlcAgentV3, usdHdlcAgentV2=usdHdlcAgentV2, PYSNMP_MODULE_ID=usdHdlcAgent, usdHdlcAgent=usdHdlcAgent, usdHdlcAgentV1=usdHdlcAgentV1)
