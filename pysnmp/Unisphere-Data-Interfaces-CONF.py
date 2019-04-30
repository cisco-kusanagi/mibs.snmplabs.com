#
# PySNMP MIB module Unisphere-Data-Interfaces-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Interfaces-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifAlias, ifStackGroup2, ifPacketGroup, ifGeneralInformationGroup, ifCounterDiscontinuityGroup, linkUpDownNotificationsGroup, ifStackStatus, ifVHCPacketGroup, ifHCFixedLengthGroup, ifFixedLengthGroup, ifHCPacketGroup = mibBuilder.importSymbols("IF-MIB", "ifAlias", "ifStackGroup2", "ifPacketGroup", "ifGeneralInformationGroup", "ifCounterDiscontinuityGroup", "linkUpDownNotificationsGroup", "ifStackStatus", "ifVHCPacketGroup", "ifHCFixedLengthGroup", "ifFixedLengthGroup", "ifHCPacketGroup")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, IpAddress, Counter32, iso, ModuleIdentity, NotificationType, Unsigned32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "IpAddress", "Counter32", "iso", "ModuleIdentity", "NotificationType", "Unsigned32", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdIfGroup, usdIfInvStackGroup = mibBuilder.importSymbols("Unisphere-Data-IF-MIB", "usdIfGroup", "usdIfInvStackGroup")
usdInterfacesAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20))
usdInterfacesAgent.setRevisions(('2001-04-27 14:24',))
if mibBuilder.loadTexts: usdInterfacesAgent.setLastUpdated('200104271424Z')
if mibBuilder.loadTexts: usdInterfacesAgent.setOrganization('Unisphere Networks, Inc.')
usdInterfacesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInterfacesAgentV1 = usdInterfacesAgentV1.setProductRelease('Version 1 of the Interfaces component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Interfaces component is supported in\n        the Unisphere RX 1.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInterfacesAgentV1 = usdInterfacesAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Interfaces-CONF", usdInterfacesAgentV1=usdInterfacesAgentV1, PYSNMP_MODULE_ID=usdInterfacesAgent, usdInterfacesAgent=usdInterfacesAgent)
