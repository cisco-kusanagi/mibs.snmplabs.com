#
# PySNMP MIB module Unisphere-Data-V35-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-V35-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:26:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Gauge32, ObjectIdentity, Bits, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, iso, Counter64, ModuleIdentity, TimeTicks, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Bits", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "iso", "Counter64", "ModuleIdentity", "TimeTicks", "IpAddress", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdV35Group, = mibBuilder.importSymbols("Unisphere-Data-V35-MIB", "usdV35Group")
usdV35Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 54))
usdV35Agent.setRevisions(('2002-01-25 21:43',))
if mibBuilder.loadTexts: usdV35Agent.setLastUpdated('200201252143Z')
if mibBuilder.loadTexts: usdV35Agent.setOrganization('Unisphere Networks, Inc.')
usdV35AgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 54, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdV35AgentV1 = usdV35AgentV1.setProductRelease('Version 1 of the X.21/V.35 component of the Unisphere Routing Switch\n        SNMP agent.  This version of the X.21/V.35 component is supported in the\n        Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdV35AgentV1 = usdV35AgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-V35-CONF", usdV35Agent=usdV35Agent, usdV35AgentV1=usdV35AgentV1, PYSNMP_MODULE_ID=usdV35Agent)
