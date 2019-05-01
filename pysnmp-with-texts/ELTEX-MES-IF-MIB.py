#
# PySNMP MIB module ELTEX-MES-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:01:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
eltMesIfMIB, = mibBuilder.importSymbols("ELTEX-MES-MIB-2", "eltMesIfMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Bits, Counter32, Counter64, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, TimeTicks, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Counter32", "Counter64", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "TimeTicks", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltMesIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1))
mibBuilder.exportSymbols("ELTEX-MES-IF-MIB", eltMesIfMIBObjects=eltMesIfMIBObjects)
