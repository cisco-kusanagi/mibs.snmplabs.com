#
# PySNMP MIB module Unisphere-Data-V35-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-V35-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:33:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ModuleIdentity, Bits, Counter64, Gauge32, IpAddress, MibIdentifier, TimeTicks, ObjectIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter64", "Gauge32", "IpAddress", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdV35Group, = mibBuilder.importSymbols("Unisphere-Data-V35-MIB", "usdV35Group")
usdV35Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 54))
usdV35Agent.setRevisions(('2002-01-25 21:43',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdV35Agent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdV35Agent.setLastUpdated('200201252143Z')
if mibBuilder.loadTexts: usdV35Agent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdV35Agent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdV35Agent.setDescription('The agent capabilities definitions for the X.21/V.35 server component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdV35AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 54, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdV35AgentV1 = usdV35AgentV1.setProductRelease('Version 1 of the X.21/V.35 component of the Unisphere Routing Switch\n        SNMP agent.  This version of the X.21/V.35 component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdV35AgentV1 = usdV35AgentV1.setStatus('current')
if mibBuilder.loadTexts: usdV35AgentV1.setDescription('The MIB supported by the SNMP agent for the X.21/V.35 application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-V35-CONF", usdV35Agent=usdV35Agent, PYSNMP_MODULE_ID=usdV35Agent, usdV35AgentV1=usdV35AgentV1)
