#
# PySNMP MIB module ADTRAN-ATLAS-HSSI-V35-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-ATLAS-HSSI-V35-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:59:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adATLASModuleInfoFPStatus, = mibBuilder.importSymbols("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus")
adATLASUnitSlotAddress, adATLASUnitFPStatus, adATLASUnitPortAddress = mibBuilder.importSymbols("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress", "adATLASUnitFPStatus", "adATLASUnitPortAddress")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Integer32, Counter64, IpAddress, ModuleIdentity, ObjectIdentity, iso, Unsigned32, Counter32, MibIdentifier, NotificationType, NotificationType, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Integer32", "Counter64", "IpAddress", "ModuleIdentity", "ObjectIdentity", "iso", "Unsigned32", "Counter32", "MibIdentifier", "NotificationType", "NotificationType", "enterprises", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adtran = MibIdentifier((1, 3, 6, 1, 4, 1, 664))
adMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2))
adATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154))
adGenATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1))
adATLASHSSIV35mg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 11))
adATLASHSSIV35IfceDeact = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15401100)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
adATLASHSSIV35IfceReact = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15401101)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
mibBuilder.exportSymbols("ADTRAN-ATLAS-HSSI-V35-MIB", adtran=adtran, adMgmt=adMgmt, adATLASHSSIV35IfceReact=adATLASHSSIV35IfceReact, adGenATLASmg=adGenATLASmg, adATLASmg=adATLASmg, adATLASHSSIV35IfceDeact=adATLASHSSIV35IfceDeact, adATLASHSSIV35mg=adATLASHSSIV35mg)
