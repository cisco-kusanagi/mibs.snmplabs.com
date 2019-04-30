#
# PySNMP MIB module ELTEX-MES-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:46:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
eltMesIfMIB, = mibBuilder.importSymbols("ELTEX-MES-MIB-2", "eltMesIfMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, IpAddress, NotificationType, MibIdentifier, Counter64, Counter32, Unsigned32, iso, TimeTicks, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "IpAddress", "NotificationType", "MibIdentifier", "Counter64", "Counter32", "Unsigned32", "iso", "TimeTicks", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltMesIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1))
mibBuilder.exportSymbols("ELTEX-MES-IF-MIB", eltMesIfMIBObjects=eltMesIfMIBObjects)
