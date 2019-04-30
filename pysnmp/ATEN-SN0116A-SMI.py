#
# PySNMP MIB module ATEN-SN0116A-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATEN-SN0116A-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
sn3101, = mibBuilder.importSymbols("ATEN-PRODUCTS-MIB", "sn3101")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, MibIdentifier, Bits, Integer32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Gauge32, Unsigned32, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibIdentifier", "Bits", "Integer32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Gauge32", "Unsigned32", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rs232 = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 1))
usrcfg = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 2))
session = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 3))
imageCurrentVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 4))
imageNewVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 5))
portAlert = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2, 6))
mibBuilder.exportSymbols("ATEN-SN0116A-SMI", rs232=rs232, imageCurrentVersion=imageCurrentVersion, portAlert=portAlert, session=session, usrcfg=usrcfg, imageNewVersion=imageNewVersion)
