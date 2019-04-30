#
# PySNMP MIB module OASUBSCR-CFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OASUBSCR-CFG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:22:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, IpAddress, ModuleIdentity, MibIdentifier, Counter64, Integer32, Unsigned32, ObjectIdentity, Counter32, NotificationType, NotificationType, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "IpAddress", "ModuleIdentity", "MibIdentifier", "Counter64", "Integer32", "Unsigned32", "ObjectIdentity", "Counter32", "NotificationType", "NotificationType", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class SubscriberName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(2, 35)

class DirectionType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("ingress", 2), ("egress", 3))

class AccountCouter(Counter32):
    pass

class AccountCounter64(Counter64):
    pass

nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 629))
nbSwitchG1 = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1))
nbSwitchG1Il = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50))
oaSubscriberConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 15))
oaSubscrConfigGen = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 1))
oaSubscrAccounting = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6))
oaSubscrAccNameTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10), )
if mibBuilder.loadTexts: oaSubscrAccNameTable.setStatus('mandatory')
oaSubscrAccNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1), ).setIndexNames((0, "OASUBSCR-CFG-MIB", "oaSubscrName"), (0, "OASUBSCR-CFG-MIB", "oaSubscrDirection"))
if mibBuilder.loadTexts: oaSubscrAccNameEntry.setStatus('mandatory')
oaSubscrName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 1), SubscriberName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrName.setStatus('mandatory')
oaSubscrDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 2), DirectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrDirection.setStatus('mandatory')
oaSubscrAccNmAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("enable", 2), ("disable", 3), ("pause", 4), ("resume", 5), ("clear", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaSubscrAccNmAdminStatus.setStatus('mandatory')
oaSubscrAccNmOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("paused", 3), ("disabled", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmOperStatus.setStatus('mandatory')
oaSubscrAccNmConformingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 6), AccountCouter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmConformingBytes.setStatus('mandatory')
oaSubscrAccNmHighConformingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmHighConformingBytes.setStatus('mandatory')
oaSubscrAccNmLowConformingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmLowConformingBytes.setStatus('mandatory')
oaSubscrAccNmExceedingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 9), AccountCouter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmExceedingBytes.setStatus('mandatory')
oaSubscrAccNmHighExceedingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmHighExceedingBytes.setStatus('mandatory')
oaSubscrAccNmLowExceedingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmLowExceedingBytes.setStatus('mandatory')
oaSubscrAccNmConformingPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 12), AccountCouter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmConformingPackets.setStatus('mandatory')
oaSubscrAccNmHighConformingPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmHighConformingPackets.setStatus('mandatory')
oaSubscrAccNmLowConformingPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmLowConformingPackets.setStatus('mandatory')
oaSubscrAccNmExceedingPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 15), AccountCouter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmExceedingPackets.setStatus('mandatory')
oaSubscrAccNmHighExceedingPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmHighExceedingPackets.setStatus('mandatory')
oaSubscrAccNmLowExceedingPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNmLowExceedingPackets.setStatus('mandatory')
oaSubscrAccNm64ConformingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 18), AccountCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNm64ConformingBytes.setStatus('mandatory')
oaSubscrAccNm64ExceedingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 15, 6, 10, 1, 19), AccountCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSubscrAccNm64ExceedingBytes.setStatus('mandatory')
mibBuilder.exportSymbols("OASUBSCR-CFG-MIB", DirectionType=DirectionType, oaSubscrAccNm64ConformingBytes=oaSubscrAccNm64ConformingBytes, oaSubscrAccNmAdminStatus=oaSubscrAccNmAdminStatus, nbSwitchG1=nbSwitchG1, oaSubscrAccNm64ExceedingBytes=oaSubscrAccNm64ExceedingBytes, SubscriberName=SubscriberName, oaSubscrConfigGen=oaSubscrConfigGen, oaSubscrAccNmHighExceedingPackets=oaSubscrAccNmHighExceedingPackets, oaSubscrAccNmOperStatus=oaSubscrAccNmOperStatus, oaSubscrAccNmConformingBytes=oaSubscrAccNmConformingBytes, oaSubscriberConfig=oaSubscriberConfig, oaSubscrAccNmConformingPackets=oaSubscrAccNmConformingPackets, oaSubscrAccNameEntry=oaSubscrAccNameEntry, AccountCounter64=AccountCounter64, oaSubscrAccNmExceedingPackets=oaSubscrAccNmExceedingPackets, nbSwitchG1Il=nbSwitchG1Il, oaSubscrAccNmExceedingBytes=oaSubscrAccNmExceedingBytes, oaSubscrAccNmLowConformingPackets=oaSubscrAccNmLowConformingPackets, oaSubscrAccNmLowExceedingPackets=oaSubscrAccNmLowExceedingPackets, oaSubscrAccNmLowConformingBytes=oaSubscrAccNmLowConformingBytes, oaSubscrAccounting=oaSubscrAccounting, oaSubscrAccNmHighConformingBytes=oaSubscrAccNmHighConformingBytes, oaSubscrAccNmLowExceedingBytes=oaSubscrAccNmLowExceedingBytes, oaSubscrAccNmHighConformingPackets=oaSubscrAccNmHighConformingPackets, oaSubscrAccNameTable=oaSubscrAccNameTable, oaSubscrDirection=oaSubscrDirection, oaSubscrAccNmHighExceedingBytes=oaSubscrAccNmHighExceedingBytes, oaSubscrName=oaSubscrName, AccountCouter=AccountCouter, nbase=nbase)
