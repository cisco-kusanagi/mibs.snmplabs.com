#
# PySNMP MIB module MSFT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSFT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, Counter64, ObjectIdentity, IpAddress, Integer32, enterprises, NotificationType, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "Integer32", "enterprises", "NotificationType", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
microsoft = MibIdentifier((1, 3, 6, 1, 4, 1, 311))
software = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1))
os = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3))
windowsNT = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1))
windows = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 2))
workstation = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1))
server = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 2))
dc = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 3))
mibBuilder.exportSymbols("MSFT-MIB", windowsNT=windowsNT, dc=dc, os=os, workstation=workstation, server=server, microsoft=microsoft, windows=windows, software=software, systems=systems)
