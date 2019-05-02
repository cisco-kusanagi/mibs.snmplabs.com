#
# PySNMP MIB module AT-CAPABILITIES (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-CAPABILITIES
# Produced by pysmi-0.3.4 at Wed May  1 11:29:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
atRouter, atAgents = mibBuilder.importSymbols("AT-SMI-MIB", "atRouter", "atAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, ModuleIdentity, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, NotificationType, ObjectIdentity, Unsigned32, Integer32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "ModuleIdentity", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atrRapier = AgentCapabilities((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atrRapier = atrRapier.setProductRelease('AT Rapier switch, release 2.9.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atrRapier = atrRapier.setStatus('current')
if mibBuilder.loadTexts: atrRapier.setDescription('Capabilities of AT Rapier switch, release 2.9.1 and later releases.')
mibBuilder.exportSymbols("AT-CAPABILITIES", atrRapier=atrRapier)
