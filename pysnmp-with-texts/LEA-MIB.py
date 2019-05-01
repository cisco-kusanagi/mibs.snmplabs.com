#
# PySNMP MIB module LEA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:06:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, iso, Gauge32, ObjectIdentity, Counter64, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, ModuleIdentity, enterprises, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "Gauge32", "ObjectIdentity", "Counter64", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "ModuleIdentity", "enterprises", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lea = ModuleIdentity((1, 3, 6, 1, 4, 1, 14841))
lea.setRevisions(('2002-09-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lea.setRevisionsDescriptions(('Beta 1',))
if mibBuilder.loadTexts: lea.setLastUpdated('2002100400Z')
if mibBuilder.loadTexts: lea.setOrganization('www.leacom.fr')
if mibBuilder.loadTexts: lea.setContactInfo('postal: Regis Urvoy 52/54 rue du capitaine Guynemer 92415 Courbevoie Cedex France email: regis.urvoy@leacom.fr')
if mibBuilder.loadTexts: lea.setDescription('Top-level infrastructure of the LEA enterprise MIB tree')
leaSplitters = MibIdentifier((1, 3, 6, 1, 4, 1, 14841, 1))
leaExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 14841, 9999))
mibBuilder.exportSymbols("LEA-MIB", leaExperimental=leaExperimental, PYSNMP_MODULE_ID=lea, leaSplitters=leaSplitters, lea=lea)
