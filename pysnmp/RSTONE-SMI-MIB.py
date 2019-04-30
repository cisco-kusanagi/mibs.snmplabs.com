#
# PySNMP MIB module RSTONE-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RSTONE-SMI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Gauge32, Bits, Integer32, enterprises, Counter64, IpAddress, NotificationType, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Gauge32", "Bits", "Integer32", "enterprises", "Counter64", "IpAddress", "NotificationType", "Counter32", "Unsigned32")
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
mibBuilder.exportSymbols("RSTONE-SMI-MIB", riverstoneMibs=riverstoneMibs, riverstoneNetworks=riverstoneNetworks, riverstoneAgentCapabilities=riverstoneAgentCapabilities, PYSNMP_MODULE_ID=riverstoneNetworks, riverstoneProducts=riverstoneProducts)
