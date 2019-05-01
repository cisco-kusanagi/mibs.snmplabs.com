#
# PySNMP MIB module Juniper-Fractional-T1-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Fractional-T1-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
TimeTicks, Counter64, ModuleIdentity, ObjectIdentity, IpAddress, Integer32, Gauge32, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Integer32", "Gauge32", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniFractionalT1Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16))
juniFractionalT1Agent.setRevisions(('2002-09-06 16:54', '2001-03-29 22:03',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniFractionalT1Agent.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniFractionalT1Agent.setLastUpdated('200209061654Z')
if mibBuilder.loadTexts: juniFractionalT1Agent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniFractionalT1Agent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniFractionalT1Agent.setDescription('The agent capabilities definitions for the Fractional T1 component of the SNMP agent in the Juniper E-series family of products.')
juniFractionalT1AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFractionalT1AgentV1 = juniFractionalT1AgentV1.setProductRelease('Version 1 of the Fractional T1 component of the JUNOSe SNMP agent.\n        This version of the Fractional T1 component was supported in JUNOSe 1.0\n        system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFractionalT1AgentV1 = juniFractionalT1AgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniFractionalT1AgentV1.setDescription('The MIB supported by the SNMP agent for the Fractional T1 application in JUNOSe. These capabilities became obsolete when juniFt1IfDataPolarity was obsoleted.')
juniFractionalT1AgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFractionalT1AgentV2 = juniFractionalT1AgentV2.setProductRelease('Version 2 of the Fractional T1 component of the JUNOSe SNMP agent.\n        This version of the Fractional T1 component is supported in JUNOSe 1.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFractionalT1AgentV2 = juniFractionalT1AgentV2.setStatus('current')
if mibBuilder.loadTexts: juniFractionalT1AgentV2.setDescription('The MIB supported by the SNMP agent for the Fractional T1 application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Fractional-T1-CONF", PYSNMP_MODULE_ID=juniFractionalT1Agent, juniFractionalT1Agent=juniFractionalT1Agent, juniFractionalT1AgentV1=juniFractionalT1AgentV1, juniFractionalT1AgentV2=juniFractionalT1AgentV2)
