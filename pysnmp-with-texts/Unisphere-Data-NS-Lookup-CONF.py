#
# PySNMP MIB module Unisphere-Data-NS-Lookup-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-NS-Lookup-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
lookupGroup, = mibBuilder.importSymbols("DISMAN-NSLOOKUP-MIB", "lookupGroup")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibIdentifier, iso, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Integer32, Unsigned32, IpAddress, Counter32, Bits, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Integer32", "Unsigned32", "IpAddress", "Counter32", "Bits", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdNsLookupAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 27))
usdNsLookupAgent.setRevisions(('2001-03-28 22:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdNsLookupAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdNsLookupAgent.setLastUpdated('200103282222Z')
if mibBuilder.loadTexts: usdNsLookupAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdNsLookupAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdNsLookupAgent.setDescription('The agent capabilities definitions for the remote name server (NS) lookup component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdNsLookupAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 27, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdNsLookupAgentV1 = usdNsLookupAgentV1.setProductRelease('Version 1 of the NS Lookup component of the Unisphere Routing Switch\n        SNMP agent.  This version of the NS Lookup component is supported in\n        the Unisphere RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdNsLookupAgentV1 = usdNsLookupAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdNsLookupAgentV1.setDescription('The MIB supported by the SNMP agent for the NS Lookup application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-NS-Lookup-CONF", usdNsLookupAgent=usdNsLookupAgent, PYSNMP_MODULE_ID=usdNsLookupAgent, usdNsLookupAgentV1=usdNsLookupAgentV1)
