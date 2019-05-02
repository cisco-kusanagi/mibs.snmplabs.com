#
# PySNMP MIB module HDSLGT2030-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HDSLGT2030-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
hdslGT2030, = mibBuilder.importSymbols("GDCHDSL-MIB", "hdslGT2030")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, MibIdentifier, Integer32, IpAddress, NotificationType, Gauge32, TimeTicks, Bits, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "MibIdentifier", "Integer32", "IpAddress", "NotificationType", "Gauge32", "TimeTicks", "Bits", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hdslGT2030System = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 1))
hdslGT2030Version = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 1, 1))
gdcGT2030SystemMIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 11, 26, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdcGT2030SystemMIBversion.setStatus('mandatory')
if mibBuilder.loadTexts: gdcGT2030SystemMIBversion.setDescription("Identifies the version of the MIB. The format of the version is x.yzT, where 'x' identifies the major revision number, 'y' identifies the minor revision number, 'z' identifies the typographical revision, and T identifies the test revision. Acceptable values for the individual revision components are as follows: x: 1 - 9 y: 0 - 9 z: 0 - 9 T: A - Z Upon formal release, no designation for the test revision will be present.")
hdslGT2030Alarms = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2))
hdslGT2030NoResponseAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 1))
hdslGT2030DiagRxErrAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 2))
hdslGT2030PowerUpAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 3))
hdslGT2030UnitFailure = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 4))
hdslGT2030ChecksumCorrupt = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 5))
hdslGT2030LossofSignal = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 6))
hdslGT2030UnavailableSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 7))
hdslGT2030ErrorSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 8))
hdslGT2030LossofSyncWord = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 9))
hdslGT2030MajorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 10))
hdslGT2030MinorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 26, 2, 11))
mibBuilder.exportSymbols("HDSLGT2030-MIB", hdslGT2030ErrorSec=hdslGT2030ErrorSec, hdslGT2030Alarms=hdslGT2030Alarms, hdslGT2030Version=hdslGT2030Version, hdslGT2030PowerUpAlm=hdslGT2030PowerUpAlm, hdslGT2030LossofSignal=hdslGT2030LossofSignal, hdslGT2030MajorBER=hdslGT2030MajorBER, hdslGT2030MinorBER=hdslGT2030MinorBER, gdcGT2030SystemMIBversion=gdcGT2030SystemMIBversion, hdslGT2030NoResponseAlm=hdslGT2030NoResponseAlm, hdslGT2030UnitFailure=hdslGT2030UnitFailure, hdslGT2030DiagRxErrAlm=hdslGT2030DiagRxErrAlm, hdslGT2030UnavailableSec=hdslGT2030UnavailableSec, hdslGT2030ChecksumCorrupt=hdslGT2030ChecksumCorrupt, hdslGT2030LossofSyncWord=hdslGT2030LossofSyncWord, hdslGT2030System=hdslGT2030System)
