#
# PySNMP MIB module SAF-ENTERPRISE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAF-ENTERPRISE
# Produced by pysmi-0.3.4 at Wed May  1 14:59:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Counter32, Bits, iso, Gauge32, Unsigned32, IpAddress, MibIdentifier, enterprises, TimeTicks, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter32", "Bits", "iso", "Gauge32", "Unsigned32", "IpAddress", "MibIdentifier", "enterprises", "TimeTicks", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
saf = ModuleIdentity((1, 3, 6, 1, 4, 1, 7571))
if mibBuilder.loadTexts: saf.setLastUpdated('2007040300Z')
if mibBuilder.loadTexts: saf.setOrganization('SAF Tehnika')
if mibBuilder.loadTexts: saf.setContactInfo('SAF Tehnika technical support <techsupport@saftehnika.com>')
if mibBuilder.loadTexts: saf.setDescription('')
tehnika = ObjectIdentity((1, 3, 6, 1, 4, 1, 7571, 100))
if mibBuilder.loadTexts: tehnika.setStatus('current')
if mibBuilder.loadTexts: tehnika.setDescription('Subtree to register SAF tehnika modules')
microwaveRadio = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1))
pointToPoint = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1))
mibBuilder.exportSymbols("SAF-ENTERPRISE", tehnika=tehnika, PYSNMP_MODULE_ID=saf, microwaveRadio=microwaveRadio, pointToPoint=pointToPoint, saf=saf)
