#
# PySNMP MIB module ATEN-SN0116A-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATEN-SN0116A-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:30:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
sn3101, = mibBuilder.importSymbols("ATEN-PRODUCTS-MIB", "sn3101")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Counter32, Integer32, Gauge32, NotificationType, iso, TimeTicks, Counter64, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Counter32", "Integer32", "Gauge32", "NotificationType", "iso", "TimeTicks", "Counter64", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rs232 = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 1))
usrcfg = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 2))
session = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 3))
imageCurrentVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 4))
imageNewVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 5))
portAlert = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 6))
mibBuilder.exportSymbols("ATEN-SN0116A-SMI", rs232=rs232, portAlert=portAlert, imageNewVersion=imageNewVersion, imageCurrentVersion=imageCurrentVersion, session=session, usrcfg=usrcfg)
