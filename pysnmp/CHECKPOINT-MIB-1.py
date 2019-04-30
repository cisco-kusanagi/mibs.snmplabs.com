#
# PySNMP MIB module CHECKPOINT-MIB-1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CHECKPOINT-MIB-1
# Produced by pysmi-0.3.4 at Mon Apr 29 17:31:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, MibIdentifier, TimeTicks, Counter32, Gauge32, Counter64, IpAddress, enterprises, iso, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Counter32", "Gauge32", "Counter64", "IpAddress", "enterprises", "iso", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

class PhysAddress(OctetString):
    pass

checkpoint = MibIdentifier((1, 3, 6, 1, 4, 1, 1919))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1919, 1))
fw = MibIdentifier((1, 3, 6, 1, 4, 1, 1919, 1, 1))
fwModuleState = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwModuleState.setStatus('mandatory')
fwFilterName = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwFilterName.setStatus('mandatory')
fwFilterDate = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwFilterDate.setStatus('mandatory')
fwAccepted = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwAccepted.setStatus('mandatory')
fwRejected = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwRejected.setStatus('mandatory')
fwDropped = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDropped.setStatus('mandatory')
fwLogged = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwLogged.setStatus('mandatory')
fwMajor = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwMajor.setStatus('mandatory')
fwMinor = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwMinor.setStatus('mandatory')
fwProduct = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwProduct.setStatus('mandatory')
fwEvent = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwEvent.setStatus('mandatory')
mibBuilder.exportSymbols("CHECKPOINT-MIB-1", PhysAddress=PhysAddress, fwMinor=fwMinor, fwModuleState=fwModuleState, fwMajor=fwMajor, products=products, fwRejected=fwRejected, fwFilterName=fwFilterName, fwAccepted=fwAccepted, fwLogged=fwLogged, fwDropped=fwDropped, fwEvent=fwEvent, DisplayString=DisplayString, fwFilterDate=fwFilterDate, checkpoint=checkpoint, fw=fw, fwProduct=fwProduct)
