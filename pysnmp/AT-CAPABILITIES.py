#
# PySNMP MIB module AT-CAPABILITIES (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-CAPABILITIES
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
atAgents, atRouter = mibBuilder.importSymbols("AT-SMI-MIB", "atAgents", "atRouter")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, Counter32, Counter64, ModuleIdentity, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, IpAddress, MibIdentifier, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "Counter32", "Counter64", "ModuleIdentity", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "IpAddress", "MibIdentifier", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atrRapier = AgentCapabilities((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atrRapier = atrRapier.setProductRelease('AT Rapier switch, release 2.9.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atrRapier = atrRapier.setStatus('current')
mibBuilder.exportSymbols("AT-CAPABILITIES", atrRapier=atrRapier)
