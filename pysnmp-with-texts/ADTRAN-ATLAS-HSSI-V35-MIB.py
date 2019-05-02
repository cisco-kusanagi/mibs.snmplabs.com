#
# PySNMP MIB module ADTRAN-ATLAS-HSSI-V35-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-ATLAS-HSSI-V35-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:14:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adATLASModuleInfoFPStatus, = mibBuilder.importSymbols("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus")
adATLASUnitFPStatus, adATLASUnitSlotAddress, adATLASUnitPortAddress = mibBuilder.importSymbols("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus", "adATLASUnitSlotAddress", "adATLASUnitPortAddress")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, enterprises, Counter64, Gauge32, NotificationType, Bits, TimeTicks, ObjectIdentity, ModuleIdentity, IpAddress, Integer32, Unsigned32, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "enterprises", "Counter64", "Gauge32", "NotificationType", "Bits", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Integer32", "Unsigned32", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adtran = MibIdentifier((1, 3, 6, 1, 4, 1, 664))
adMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2))
adATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154))
adGenATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1))
adATLASHSSIV35mg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 11))
adATLASHSSIV35IfceDeact = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15401100)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
if mibBuilder.loadTexts: adATLASHSSIV35IfceDeact.setDescription('This trap indicates a HSSI/V.35 interface has been deactivated because the number of active DS1 links has fallen below the user-defined threshold value.')
adATLASHSSIV35IfceReact = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15401101)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
if mibBuilder.loadTexts: adATLASHSSIV35IfceReact.setDescription('This trap indicates a HSSI/V.35 interface has been reactivated because either the number of active DS1 links has risen above the user-defined threshold value or because the user has manually reactivated it.')
mibBuilder.exportSymbols("ADTRAN-ATLAS-HSSI-V35-MIB", adATLASHSSIV35mg=adATLASHSSIV35mg, adGenATLASmg=adGenATLASmg, adATLASmg=adATLASmg, adATLASHSSIV35IfceDeact=adATLASHSSIV35IfceDeact, adATLASHSSIV35IfceReact=adATLASHSSIV35IfceReact, adtran=adtran, adMgmt=adMgmt)
