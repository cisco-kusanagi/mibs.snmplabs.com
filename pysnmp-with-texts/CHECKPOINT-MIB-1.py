#
# PySNMP MIB module CHECKPOINT-MIB-1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CHECKPOINT-MIB-1
# Produced by pysmi-0.3.4 at Wed May  1 11:48:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, Integer32, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Unsigned32, MibIdentifier, enterprises, ObjectIdentity, Counter32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Integer32", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Unsigned32", "MibIdentifier", "enterprises", "ObjectIdentity", "Counter32", "Gauge32", "Counter64")
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
if mibBuilder.loadTexts: fwModuleState.setDescription('The state of the fw module.')
fwFilterName = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwFilterName.setStatus('mandatory')
if mibBuilder.loadTexts: fwFilterName.setDescription('The name of the loaded filter.')
fwFilterDate = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwFilterDate.setStatus('mandatory')
if mibBuilder.loadTexts: fwFilterDate.setDescription('When was the filter installed (STRING!)')
fwAccepted = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwAccepted.setStatus('mandatory')
if mibBuilder.loadTexts: fwAccepted.setDescription('The number of accepted packets.')
fwRejected = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwRejected.setStatus('mandatory')
if mibBuilder.loadTexts: fwRejected.setDescription('The number of rejected packets.')
fwDropped = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDropped.setStatus('mandatory')
if mibBuilder.loadTexts: fwDropped.setDescription('The number of dropped packets.')
fwLogged = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwLogged.setStatus('mandatory')
if mibBuilder.loadTexts: fwLogged.setDescription('The number of logged packets.')
fwMajor = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwMajor.setStatus('mandatory')
if mibBuilder.loadTexts: fwMajor.setDescription('FireWall-1 Major Version.')
fwMinor = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwMinor.setStatus('mandatory')
if mibBuilder.loadTexts: fwMinor.setDescription('FireWall-1 Minor Version.')
fwProduct = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwProduct.setStatus('mandatory')
if mibBuilder.loadTexts: fwProduct.setDescription('FireWall-1 Product.')
fwEvent = MibScalar((1, 3, 6, 1, 4, 1, 1919, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwEvent.setStatus('mandatory')
if mibBuilder.loadTexts: fwEvent.setDescription('A string containing the last snmp trap sent via fw')
mibBuilder.exportSymbols("CHECKPOINT-MIB-1", fwModuleState=fwModuleState, checkpoint=checkpoint, fwFilterName=fwFilterName, fwProduct=fwProduct, fwAccepted=fwAccepted, fw=fw, fwRejected=fwRejected, DisplayString=DisplayString, fwEvent=fwEvent, PhysAddress=PhysAddress, fwMajor=fwMajor, fwMinor=fwMinor, fwLogged=fwLogged, products=products, fwDropped=fwDropped, fwFilterDate=fwFilterDate)
