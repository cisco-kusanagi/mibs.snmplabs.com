#
# PySNMP MIB module Juniper-Fractional-T1-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Fractional-T1-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, iso, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, MibIdentifier, Counter32, IpAddress, Counter64, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "iso", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter32", "IpAddress", "Counter64", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniFractionalT1Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16))
juniFractionalT1Agent.setRevisions(('2002-09-06 16:54', '2001-03-29 22:03',))
if mibBuilder.loadTexts: juniFractionalT1Agent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniFractionalT1Agent.setOrganization('Juniper Networks, Inc.')
juniFractionalT1AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFractionalT1AgentV1 = juniFractionalT1AgentV1.setProductRelease('Version 1 of the Fractional T1 component of the JUNOSe SNMP agent.\n        This version of the Fractional T1 component was supported in JUNOSe 1.0\n        system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFractionalT1AgentV1 = juniFractionalT1AgentV1.setStatus('obsolete')
juniFractionalT1AgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFractionalT1AgentV2 = juniFractionalT1AgentV2.setProductRelease('Version 2 of the Fractional T1 component of the JUNOSe SNMP agent.\n        This version of the Fractional T1 component is supported in JUNOSe 1.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFractionalT1AgentV2 = juniFractionalT1AgentV2.setStatus('current')
mibBuilder.exportSymbols("Juniper-Fractional-T1-CONF", PYSNMP_MODULE_ID=juniFractionalT1Agent, juniFractionalT1AgentV2=juniFractionalT1AgentV2, juniFractionalT1Agent=juniFractionalT1Agent, juniFractionalT1AgentV1=juniFractionalT1AgentV1)
