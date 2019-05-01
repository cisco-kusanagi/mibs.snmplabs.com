#
# PySNMP MIB module Unisphere-Data-CBF-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-CBF-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:30:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, ObjectIdentity, NotificationType, Counter64, Bits, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Unsigned32, MibIdentifier, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "NotificationType", "Counter64", "Bits", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Unsigned32", "MibIdentifier", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdCbfGroup, = mibBuilder.importSymbols("Unisphere-Data-CBF-MIB", "usdCbfGroup")
usdCbfAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 48))
usdCbfAgent.setRevisions(('2001-03-29 20:23',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdCbfAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdCbfAgent.setLastUpdated('200103292023Z')
if mibBuilder.loadTexts: usdCbfAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdCbfAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdCbfAgent.setDescription('The agent capabilities definitions for the Connection-Based Forwarding (CBF) protocol management component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdCbfAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 48, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCbfAgentV1 = usdCbfAgentV1.setProductRelease('Version 1 of the Connection-Based Forwarding (CBF) component of the\n        Unisphere Routing Switch SNMP agent.  This version of the CBF component\n        is supported in the Unisphere RX 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCbfAgentV1 = usdCbfAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdCbfAgentV1.setDescription('The MIB supported by the SNMP agent for the CBF application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-CBF-CONF", PYSNMP_MODULE_ID=usdCbfAgent, usdCbfAgentV1=usdCbfAgentV1, usdCbfAgent=usdCbfAgent)
