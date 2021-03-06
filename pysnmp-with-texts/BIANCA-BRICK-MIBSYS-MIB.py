#
# PySNMP MIB module BIANCA-BRICK-MIBSYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-MIBSYS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:38:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, Integer32, Bits, TimeTicks, Counter64, NotificationType, Gauge32, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Integer32", "Bits", "TimeTicks", "Counter64", "NotificationType", "Gauge32", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
sys = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17))
sysPCMTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 17, 1), )
if mibBuilder.loadTexts: sysPCMTable.setStatus('mandatory')
if mibBuilder.loadTexts: sysPCMTable.setDescription('')
sysPCMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-MIBSYS-MIB", "sysPCMSlot"), (0, "BIANCA-BRICK-MIBSYS-MIB", "sysPCMUnit"))
if mibBuilder.loadTexts: sysPCMEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sysPCMEntry.setDescription('')
sysPCMSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysPCMSlot.setStatus('mandatory')
if mibBuilder.loadTexts: sysPCMSlot.setDescription('')
sysPCMUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysPCMUnit.setStatus('mandatory')
if mibBuilder.loadTexts: sysPCMUnit.setDescription('Identification number of the used unit.')
sysPCMClockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("not-ready", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysPCMClockStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sysPCMClockStatus.setDescription("shows wether this board can supply a clock signal to the internal PCM-Highway. ready: this board can supply a clock signal not_ready: this board can't supply a clock signal")
sysPCMClockMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("candidate", 1), ("master", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysPCMClockMaster.setStatus('mandatory')
if mibBuilder.loadTexts: sysPCMClockMaster.setDescription('shows the status of this board. candidate: this board can become PCM Highway master master: this board is PCM Highway master')
sysPCMMasterPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysPCMMasterPrio.setStatus('mandatory')
if mibBuilder.loadTexts: sysPCMMasterPrio.setDescription('Priority during PCM-Highway master election. A small value results in high priority; the candidate with highest priority wins the election. Prio 128 (lowest priority) lets the PCM-Highway master use its own clock (instead of using network clock).')
sysPCMChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysPCMChanges.setStatus('mandatory')
if mibBuilder.loadTexts: sysPCMChanges.setDescription('counts how often sysPCMClockMaster has changed.')
mibBuilder.exportSymbols("BIANCA-BRICK-MIBSYS-MIB", sysPCMClockMaster=sysPCMClockMaster, enterprises=enterprises, bibo=bibo, sysPCMSlot=sysPCMSlot, sysPCMMasterPrio=sysPCMMasterPrio, dod=dod, internet=internet, bintec=bintec, private=private, sysPCMTable=sysPCMTable, sys=sys, sysPCMEntry=sysPCMEntry, sysPCMUnit=sysPCMUnit, sysPCMClockStatus=sysPCMClockStatus, org=org, sysPCMChanges=sysPCMChanges)
