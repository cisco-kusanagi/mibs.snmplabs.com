#
# PySNMP MIB module Unisphere-Data-Fractional-T1-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Fractional-T1-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, IpAddress, MibIdentifier, Counter32, NotificationType, Unsigned32, TimeTicks, Counter64, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter32", "NotificationType", "Unsigned32", "TimeTicks", "Counter64", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdFt1Group, usdFt1Group2 = mibBuilder.importSymbols("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1Group", "usdFt1Group2")
usdFractionalT1Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16))
usdFractionalT1Agent.setRevisions(('2001-03-29 22:03',))
if mibBuilder.loadTexts: usdFractionalT1Agent.setLastUpdated('200103292203Z')
if mibBuilder.loadTexts: usdFractionalT1Agent.setOrganization('Unisphere Networks, Inc.')
usdFractionalT1AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFractionalT1AgentV1 = usdFractionalT1AgentV1.setProductRelease('Version 1 of the Fractional T1 component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Fractional T1 component was\n        supported in the Unisphere RX 1.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFractionalT1AgentV1 = usdFractionalT1AgentV1.setStatus('obsolete')
usdFractionalT1AgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFractionalT1AgentV2 = usdFractionalT1AgentV2.setProductRelease('Version 2 of the Fractional T1 component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Fractional T1 component is\n        supported in the Unisphere RX 1.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFractionalT1AgentV2 = usdFractionalT1AgentV2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Fractional-T1-CONF", usdFractionalT1AgentV2=usdFractionalT1AgentV2, PYSNMP_MODULE_ID=usdFractionalT1Agent, usdFractionalT1Agent=usdFractionalT1Agent, usdFractionalT1AgentV1=usdFractionalT1AgentV1)
