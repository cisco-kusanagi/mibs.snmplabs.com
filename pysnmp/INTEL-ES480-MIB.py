#
# PySNMP MIB module INTEL-ES480-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-ES480-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:42:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, MibIdentifier, IpAddress, Unsigned32, ModuleIdentity, enterprises, NotificationType, Bits, Integer32, Counter32, iso, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "MibIdentifier", "IpAddress", "Unsigned32", "ModuleIdentity", "enterprises", "NotificationType", "Bits", "Integer32", "Counter32", "iso", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
intel = MibIdentifier((1, 3, 6, 1, 4, 1, 343))
sysProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 5))
switches = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 5, 1))
mib2ext = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6))
es480tAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 60))
es480t = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 5, 1, 15))
es480tSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 60, 1))
mibBuilder.exportSymbols("INTEL-ES480-MIB", es480tSystem=es480tSystem, es480tAgent=es480tAgent, es480t=es480t, mib2ext=mib2ext, switches=switches, sysProducts=sysProducts, intel=intel)
