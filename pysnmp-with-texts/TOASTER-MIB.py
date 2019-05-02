#
# PySNMP MIB module TOASTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TOASTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:23:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Integer32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter64, MibIdentifier, enterprises, Counter32, ModuleIdentity, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Integer32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter64", "MibIdentifier", "enterprises", "Counter32", "ModuleIdentity", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
epilogue = MibIdentifier((1, 3, 6, 1, 4, 1, 12))
toaster = MibIdentifier((1, 3, 6, 1, 4, 1, 12, 2))
toasterManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 12, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: toasterManufacturer.setStatus('mandatory')
if mibBuilder.loadTexts: toasterManufacturer.setDescription("The name of the toaster's manufacturer. For instance, Sunbeam.")
toasterModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 12, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: toasterModelNumber.setStatus('mandatory')
if mibBuilder.loadTexts: toasterModelNumber.setDescription("The name of the toaster's model. For instance, Radiant Automatic.")
toasterControl = MibScalar((1, 3, 6, 1, 4, 1, 12, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: toasterControl.setStatus('mandatory')
if mibBuilder.loadTexts: toasterControl.setDescription('This variable controls the current state of the toaster. To begin toasting, set it to down(2). To abort toasting (perhaps in the event of an emergency), set it to up(2).')
toasterDoneness = MibScalar((1, 3, 6, 1, 4, 1, 12, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: toasterDoneness.setStatus('mandatory')
if mibBuilder.loadTexts: toasterDoneness.setDescription('This variable controls how well done ensuing toast should be on a scale of 1 to 10. Toast made at 10 is generally considered unfit for human consumption; toast made at 1 is lightly warmed.')
toasterToastType = MibScalar((1, 3, 6, 1, 4, 1, 12, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("white-bread", 1), ("wheat-bread", 2), ("wonder-bread", 3), ("frozen-waffle", 4), ("frozen-bagel", 5), ("hash-brown", 6), ("other", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: toasterToastType.setStatus('mandatory')
if mibBuilder.loadTexts: toasterToastType.setDescription('This variable informs the toaster of the type of material being toasted. The toaster uses this information combined with toasterToastDoneness to compute how long the material must be toasted for to achieve the desired doneness.')
mibBuilder.exportSymbols("TOASTER-MIB", toasterControl=toasterControl, toasterToastType=toasterToastType, toaster=toaster, toasterModelNumber=toasterModelNumber, epilogue=epilogue, toasterDoneness=toasterDoneness, toasterManufacturer=toasterManufacturer)
