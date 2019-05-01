#
# PySNMP MIB module Unisphere-Data-Fractional-T1-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Fractional-T1-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibIdentifier, Gauge32, TimeTicks, Integer32, NotificationType, ModuleIdentity, ObjectIdentity, IpAddress, Counter32, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "TimeTicks", "Integer32", "NotificationType", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Counter32", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdFt1Group2, usdFt1Group = mibBuilder.importSymbols("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1Group2", "usdFt1Group")
usdFractionalT1Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16))
usdFractionalT1Agent.setRevisions(('2001-03-29 22:03',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdFractionalT1Agent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdFractionalT1Agent.setLastUpdated('200103292203Z')
if mibBuilder.loadTexts: usdFractionalT1Agent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdFractionalT1Agent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdFractionalT1Agent.setDescription('The agent capabilities definitions for the Fractional T1 component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdFractionalT1AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFractionalT1AgentV1 = usdFractionalT1AgentV1.setProductRelease('Version 1 of the Fractional T1 component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Fractional T1 component was\n        supported in the Unisphere RX 1.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFractionalT1AgentV1 = usdFractionalT1AgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdFractionalT1AgentV1.setDescription('The MIB supported by the SNMP agent for the Fractional T1 application in the Unisphere Routing Switch. These capabilities became obsolete when rsFt1IfDataPolarity was obsoleted.')
usdFractionalT1AgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 16, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFractionalT1AgentV2 = usdFractionalT1AgentV2.setProductRelease('Version 2 of the Fractional T1 component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Fractional T1 component is\n        supported in the Unisphere RX 1.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFractionalT1AgentV2 = usdFractionalT1AgentV2.setStatus('current')
if mibBuilder.loadTexts: usdFractionalT1AgentV2.setDescription('The MIB supported by the SNMP agent for the Fractional T1 application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Fractional-T1-CONF", PYSNMP_MODULE_ID=usdFractionalT1Agent, usdFractionalT1AgentV2=usdFractionalT1AgentV2, usdFractionalT1AgentV1=usdFractionalT1AgentV1, usdFractionalT1Agent=usdFractionalT1Agent)
