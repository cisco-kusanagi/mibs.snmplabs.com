#
# PySNMP MIB module PANDATEL-INAX-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANDATEL-INAX-MODEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
device_id, mdmSpecifics = mibBuilder.importSymbols("PANDATEL-MODEM-MIB", "device-id", "mdmSpecifics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, iso, IpAddress, Integer32, TimeTicks, Unsigned32, Bits, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Counter64, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "iso", "IpAddress", "Integer32", "TimeTicks", "Unsigned32", "Bits", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Counter64", "NotificationType", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
inax_modem = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 701)).setLabel("inax-modem")
inax = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701))
inaxModemTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1), )
if mibBuilder.loadTexts: inaxModemTable.setStatus('mandatory')
inaxTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1), ).setIndexNames((0, "PANDATEL-INAX-MODEM-MIB", "mdmRack"), (0, "PANDATEL-INAX-MODEM-MIB", "mdmModem"), (0, "PANDATEL-INAX-MODEM-MIB", "mdmPosition"))
if mibBuilder.loadTexts: inaxTableEntry.setStatus('mandatory')
mdmRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmRack.setStatus('mandatory')
mdmModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModem.setStatus('mandatory')
mdmPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmPosition.setStatus('mandatory')
mdmModemName = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemName.setStatus('mandatory')
mdmModemProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 99))).clone(namedValues=NamedValues(("other", 1), ("e1", 2), ("t1", 3), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemProperty.setStatus('mandatory')
mdmActiveLink = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 5, 11, 90))).clone(namedValues=NamedValues(("line-port-4", 4), ("line-port-5", 5), ("line-port-4-and-5", 11), ("disable", 90)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmActiveLink.setStatus('mandatory')
mdmRemoteAccessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 1, 1, 64), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 98, 99))).clone(namedValues=NamedValues(("via-timeslot-1", 1), ("via-timeslot-2", 2), ("via-timeslot-3", 3), ("via-timeslot-4", 4), ("via-timeslot-5", 5), ("via-timeslot-6", 6), ("via-timeslot-7", 7), ("via-timeslot-8", 8), ("via-timeslot-9", 9), ("via-timeslot-10", 10), ("via-timeslot-11", 11), ("via-timeslot-12", 12), ("via-timeslot-13", 13), ("via-timeslot-14", 14), ("via-timeslot-15", 15), ("via-timeslot-16", 16), ("via-timeslot-17", 17), ("via-timeslot-18", 18), ("via-timeslot-19", 19), ("via-timeslot-20", 20), ("via-timeslot-21", 21), ("via-timeslot-22", 22), ("via-timeslot-23", 23), ("via-timeslot-24", 24), ("via-timeslot-25", 25), ("via-timeslot-26", 26), ("via-timeslot-27", 27), ("via-timeslot-28", 28), ("via-timeslot-29", 29), ("via-timeslot-30", 30), ("via-timeslot-31", 31), ("disable", 98), ("other", 99)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmRemoteAccessMode.setStatus('mandatory')
inaxIFPortTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2), )
if mibBuilder.loadTexts: inaxIFPortTable.setStatus('mandatory')
inaxIFPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1), ).setIndexNames((0, "PANDATEL-INAX-MODEM-MIB", "iportRack"), (0, "PANDATEL-INAX-MODEM-MIB", "iportModem"), (0, "PANDATEL-INAX-MODEM-MIB", "iportPosition"), (0, "PANDATEL-INAX-MODEM-MIB", "iportPort"))
if mibBuilder.loadTexts: inaxIFPortEntry.setStatus('mandatory')
iportRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iportRack.setStatus('mandatory')
iportModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iportModem.setStatus('mandatory')
iportPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iportPosition.setStatus('mandatory')
iportPort = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iportPort.setStatus('mandatory')
iportDataEmulationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 99))).clone(namedValues=NamedValues(("other", 1), ("dte", 2), ("dce", 3), ("te", 4), ("nt", 5), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iportDataEmulationMode.setStatus('mandatory')
iportDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("off", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iportDataRate.setStatus('mandatory')
iportTimeslotSize = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("nx64k", 2), ("nx56k", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iportTimeslotSize.setStatus('mandatory')
inaxLinePortTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3), )
if mibBuilder.loadTexts: inaxLinePortTable.setStatus('mandatory')
inaxLinePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1), ).setIndexNames((0, "PANDATEL-INAX-MODEM-MIB", "lportRack"), (0, "PANDATEL-INAX-MODEM-MIB", "lportModem"), (0, "PANDATEL-INAX-MODEM-MIB", "lportPosition"), (0, "PANDATEL-INAX-MODEM-MIB", "lportPort"))
if mibBuilder.loadTexts: inaxLinePortEntry.setStatus('mandatory')
lportRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lportRack.setStatus('mandatory')
lportModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lportModem.setStatus('mandatory')
lportPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lportPosition.setStatus('mandatory')
lportPort = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lportPort.setStatus('mandatory')
lportDataEmulationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 99))).clone(namedValues=NamedValues(("other", 1), ("dte", 2), ("dce", 3), ("te", 4), ("nt", 5), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lportDataEmulationMode.setStatus('mandatory')
lportClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("internal", 2), ("remote", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lportClockSource.setStatus('mandatory')
lportDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("off", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lportDataRate.setStatus('mandatory')
lportCRC4Generation = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lportCRC4Generation.setStatus('mandatory')
lportFramingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("d4", 2), ("esf", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lportFramingMode.setStatus('mandatory')
lportCodingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 51), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("ami", 2), ("b8zs", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lportCodingMode.setStatus('mandatory')
lportLineBuiltOut = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 68), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 100))).clone(namedValues=NamedValues(("other", 1), ("itu-rec-g703", 2), ("dsx-1-0to133-ft", 3), ("dsx-1-133to266-ft", 4), ("dsx-1-266to399-ft", 5), ("dsx-1-399to533-ft", 6), ("dsx-1-533to655-ft", 7), ("csu-0db", 8), ("csu-7db5", 9), ("csu-15db", 10), ("csu-22db5", 11), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lportLineBuiltOut.setStatus('mandatory')
lportPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 69), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("if-mode", 2), ("backup-mode", 3), ("link-mode", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lportPortMode.setStatus('mandatory')
lportCRC6Test = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 100), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4, 100))).clone(namedValues=NamedValues(("other", 1), ("start", 3), ("stop", 4), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lportCRC6Test.setStatus('mandatory')
lportCRC6Status = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 101), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 5, 6, 7, 100))).clone(namedValues=NamedValues(("other", 1), ("never-started", 2), ("running", 5), ("stopped", 6), ("start-failed", 7), ("not-available", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lportCRC6Status.setStatus('mandatory')
lportCRC6Error = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 3, 1, 102), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lportCRC6Error.setStatus('mandatory')
inaxTimeslotTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4), )
if mibBuilder.loadTexts: inaxTimeslotTable.setStatus('mandatory')
inaxTimeslotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1), ).setIndexNames((0, "PANDATEL-INAX-MODEM-MIB", "tsRack"), (0, "PANDATEL-INAX-MODEM-MIB", "tsModem"), (0, "PANDATEL-INAX-MODEM-MIB", "tsPosition"), (0, "PANDATEL-INAX-MODEM-MIB", "tsPort"))
if mibBuilder.loadTexts: inaxTimeslotEntry.setStatus('mandatory')
tsRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsRack.setStatus('mandatory')
tsModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsModem.setStatus('mandatory')
tsPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsPosition.setStatus('mandatory')
tsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsPort.setStatus('mandatory')
tsTimeslot1 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 301), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot1.setStatus('mandatory')
tsTimeslot2 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 302), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot2.setStatus('mandatory')
tsTimeslot3 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 303), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot3.setStatus('mandatory')
tsTimeslot4 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 304), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot4.setStatus('mandatory')
tsTimeslot5 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 305), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot5.setStatus('mandatory')
tsTimeslot6 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 306), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot6.setStatus('mandatory')
tsTimeslot7 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 307), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot7.setStatus('mandatory')
tsTimeslot8 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 308), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot8.setStatus('mandatory')
tsTimeslot9 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 309), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot9.setStatus('mandatory')
tsTimeslot10 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 310), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot10.setStatus('mandatory')
tsTimeslot11 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 311), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot11.setStatus('mandatory')
tsTimeslot12 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 312), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot12.setStatus('mandatory')
tsTimeslot13 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 313), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot13.setStatus('mandatory')
tsTimeslot14 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 314), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot14.setStatus('mandatory')
tsTimeslot15 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 315), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot15.setStatus('mandatory')
tsTimeslot16 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 316), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot16.setStatus('mandatory')
tsTimeslot17 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 317), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot17.setStatus('mandatory')
tsTimeslot18 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 318), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot18.setStatus('mandatory')
tsTimeslot19 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 319), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot19.setStatus('mandatory')
tsTimeslot20 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 320), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot20.setStatus('mandatory')
tsTimeslot21 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 321), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot21.setStatus('mandatory')
tsTimeslot22 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 322), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot22.setStatus('mandatory')
tsTimeslot23 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 323), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot23.setStatus('mandatory')
tsTimeslot24 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 324), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot24.setStatus('mandatory')
tsTimeslot25 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 325), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot25.setStatus('mandatory')
tsTimeslot26 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 326), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot26.setStatus('mandatory')
tsTimeslot27 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 327), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot27.setStatus('mandatory')
tsTimeslot28 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 328), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot28.setStatus('mandatory')
tsTimeslot29 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 329), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot29.setStatus('mandatory')
tsTimeslot30 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 330), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot30.setStatus('mandatory')
tsTimeslot31 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 701, 4, 1, 331), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 97, 98, 99, 100))).clone(namedValues=NamedValues(("port-1", 1), ("port-2", 2), ("port-3", 3), ("port-4", 4), ("remote-access", 97), ("off", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsTimeslot31.setStatus('mandatory')
mibBuilder.exportSymbols("PANDATEL-INAX-MODEM-MIB", tsTimeslot11=tsTimeslot11, lportPort=lportPort, lportLineBuiltOut=lportLineBuiltOut, tsTimeslot21=tsTimeslot21, tsTimeslot7=tsTimeslot7, tsRack=tsRack, lportCRC6Status=lportCRC6Status, inax=inax, tsTimeslot6=tsTimeslot6, tsTimeslot19=tsTimeslot19, tsTimeslot23=tsTimeslot23, tsTimeslot1=tsTimeslot1, inaxLinePortEntry=inaxLinePortEntry, tsTimeslot25=tsTimeslot25, tsModem=tsModem, inaxModemTable=inaxModemTable, tsTimeslot26=tsTimeslot26, tsTimeslot3=tsTimeslot3, tsTimeslot28=tsTimeslot28, lportDataRate=lportDataRate, lportCRC6Test=lportCRC6Test, tsTimeslot13=tsTimeslot13, iportRack=iportRack, iportPosition=iportPosition, iportPort=iportPort, lportCRC4Generation=lportCRC4Generation, inaxLinePortTable=inaxLinePortTable, tsTimeslot31=tsTimeslot31, iportDataEmulationMode=iportDataEmulationMode, iportModem=iportModem, tsTimeslot17=tsTimeslot17, iportTimeslotSize=iportTimeslotSize, mdmActiveLink=mdmActiveLink, mdmRemoteAccessMode=mdmRemoteAccessMode, tsTimeslot24=tsTimeslot24, tsTimeslot2=tsTimeslot2, inaxIFPortTable=inaxIFPortTable, tsTimeslot20=tsTimeslot20, tsPosition=tsPosition, tsTimeslot10=tsTimeslot10, lportCRC6Error=lportCRC6Error, inax_modem=inax_modem, tsTimeslot4=tsTimeslot4, lportRack=lportRack, tsTimeslot8=tsTimeslot8, tsTimeslot18=tsTimeslot18, lportPosition=lportPosition, lportPortMode=lportPortMode, inaxTimeslotTable=inaxTimeslotTable, tsTimeslot27=tsTimeslot27, inaxTableEntry=inaxTableEntry, tsPort=tsPort, lportClockSource=lportClockSource, mdmModem=mdmModem, tsTimeslot5=tsTimeslot5, tsTimeslot29=tsTimeslot29, tsTimeslot16=tsTimeslot16, tsTimeslot14=tsTimeslot14, lportCodingMode=lportCodingMode, tsTimeslot15=tsTimeslot15, mdmPosition=mdmPosition, inaxTimeslotEntry=inaxTimeslotEntry, tsTimeslot12=tsTimeslot12, tsTimeslot22=tsTimeslot22, tsTimeslot9=tsTimeslot9, mdmRack=mdmRack, tsTimeslot30=tsTimeslot30, inaxIFPortEntry=inaxIFPortEntry, mdmModemProperty=mdmModemProperty, iportDataRate=iportDataRate, lportDataEmulationMode=lportDataEmulationMode, lportFramingMode=lportFramingMode, mdmModemName=mdmModemName, lportModem=lportModem)
