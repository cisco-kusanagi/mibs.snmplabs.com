#
# PySNMP MIB module Unisphere-Data-System-Clock-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-System-Clock-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter32, TimeTicks, IpAddress, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Gauge32, Bits, iso, ModuleIdentity, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "IpAddress", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Gauge32", "Bits", "iso", "ModuleIdentity", "MibIdentifier", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdNtpAccessGroupGroup, usdNtpClientGroup, usdNtpServerGroup, usdNtpSysClockGroup, usdSysClockDstGroup, usdNtpPeersGroup, usdSysClockTimeGroup = mibBuilder.importSymbols("Unisphere-Data-System-Clock-MIB", "usdNtpAccessGroupGroup", "usdNtpClientGroup", "usdNtpServerGroup", "usdNtpSysClockGroup", "usdSysClockDstGroup", "usdNtpPeersGroup", "usdSysClockTimeGroup")
usdSysClockAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52))
usdSysClockAgent.setRevisions(('2002-04-04 18:47',))
if mibBuilder.loadTexts: usdSysClockAgent.setLastUpdated('200204041847Z')
if mibBuilder.loadTexts: usdSysClockAgent.setOrganization('Unisphere Networks, Inc.')
usdSysClockAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSysClockAgentV1 = usdSysClockAgentV1.setProductRelease('Version 1 of the system clock component of the Unisphere Routing Switch\n        SNMP agent.  This version of the system clock component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSysClockAgentV1 = usdSysClockAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-System-Clock-CONF", PYSNMP_MODULE_ID=usdSysClockAgent, usdSysClockAgent=usdSysClockAgent, usdSysClockAgentV1=usdSysClockAgentV1)
