#
# PySNMP MIB module PANASAS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANASAS-ROOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Integer32, Unsigned32, MibIdentifier, NotificationType, ModuleIdentity, TimeTicks, Counter64, Gauge32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Integer32", "Unsigned32", "MibIdentifier", "NotificationType", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
panasas = ModuleIdentity((1, 3, 6, 1, 4, 1, 10159))
panasas.setRevisions(('2011-04-07 00:00',))
if mibBuilder.loadTexts: panasas.setLastUpdated('201104070000Z')
if mibBuilder.loadTexts: panasas.setOrganization('Panasas, Inc')
panProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1))
panNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 1))
panHw = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 2))
panFs = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3))
mibBuilder.exportSymbols("PANASAS-ROOT-MIB", panProducts=panProducts, panFs=panFs, panasas=panasas, panHw=panHw, PYSNMP_MODULE_ID=panasas, panNotifications=panNotifications)
