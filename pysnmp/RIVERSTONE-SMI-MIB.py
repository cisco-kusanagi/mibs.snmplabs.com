#
# PySNMP MIB module RIVERSTONE-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-SMI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, TimeTicks, ModuleIdentity, enterprises, NotificationType, Bits, Counter64, MibIdentifier, Counter32, IpAddress, ObjectIdentity, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "TimeTicks", "ModuleIdentity", "enterprises", "NotificationType", "Bits", "Counter64", "MibIdentifier", "Counter32", "IpAddress", "ObjectIdentity", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
riverstoneNetworks = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567))
riverstoneNetworks.setRevisions(('2000-04-15 00:00',))
if mibBuilder.loadTexts: riverstoneNetworks.setLastUpdated('200004150000Z')
if mibBuilder.loadTexts: riverstoneNetworks.setOrganization('Riverstone Networks, Inc')
riverstoneProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1))
if mibBuilder.loadTexts: riverstoneProducts.setStatus('current')
riverstoneMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 2))
if mibBuilder.loadTexts: riverstoneMibs.setStatus('current')
riverstoneAgentCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 10))
if mibBuilder.loadTexts: riverstoneAgentCapabilities.setStatus('current')
mibBuilder.exportSymbols("RIVERSTONE-SMI-MIB", riverstoneAgentCapabilities=riverstoneAgentCapabilities, riverstoneNetworks=riverstoneNetworks, riverstoneProducts=riverstoneProducts, PYSNMP_MODULE_ID=riverstoneNetworks, riverstoneMibs=riverstoneMibs)
