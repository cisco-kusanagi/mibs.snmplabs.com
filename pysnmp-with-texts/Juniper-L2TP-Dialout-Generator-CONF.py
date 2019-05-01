#
# PySNMP MIB module Juniper-L2TP-Dialout-Generator-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-L2TP-Dialout-Generator-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:03:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Bits, IpAddress, Integer32, Counter64, NotificationType, TimeTicks, Gauge32, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Bits", "IpAddress", "Integer32", "Counter64", "NotificationType", "TimeTicks", "Gauge32", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniL2tpDialoutGeneratorAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 59))
juniL2tpDialoutGeneratorAgent.setRevisions(('2002-11-21 14:51',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniL2tpDialoutGeneratorAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: juniL2tpDialoutGeneratorAgent.setLastUpdated('200211211451Z')
if mibBuilder.loadTexts: juniL2tpDialoutGeneratorAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniL2tpDialoutGeneratorAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniL2tpDialoutGeneratorAgent.setDescription('The agent capabilities definitions for the Layer 2 Tunneling Protocol (L2TP) Dialout Generator component of the SNMP agent in the Juniper E-series family of products.')
juniL2tpDialoutGeneratorAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 59, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpDialoutGeneratorAgentV1 = juniL2tpDialoutGeneratorAgentV1.setProductRelease('Version 1 of the L2TP Dialout Generator component of the JUNOSe SNMP\n        agent.  This version of the L2TP Dialout Generator component is\n        supported in JUNOSe 5.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniL2tpDialoutGeneratorAgentV1 = juniL2tpDialoutGeneratorAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniL2tpDialoutGeneratorAgentV1.setDescription('The MIB supported by the SNMP agent for the L2TP Dialout Generator application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-L2TP-Dialout-Generator-CONF", juniL2tpDialoutGeneratorAgentV1=juniL2tpDialoutGeneratorAgentV1, PYSNMP_MODULE_ID=juniL2tpDialoutGeneratorAgent, juniL2tpDialoutGeneratorAgent=juniL2tpDialoutGeneratorAgent)
