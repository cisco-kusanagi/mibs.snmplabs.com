#
# PySNMP MIB module INTEL-ES480-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-ES480-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:54:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, ObjectIdentity, IpAddress, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, enterprises, Unsigned32, NotificationType, iso, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "enterprises", "Unsigned32", "NotificationType", "iso", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
intel = MibIdentifier((1, 3, 6, 1, 4, 1, 343))
sysProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 5))
switches = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 5, 1))
mib2ext = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6))
es480tAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 60))
es480t = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 5, 1, 15))
es480tSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 60, 1))
mibBuilder.exportSymbols("INTEL-ES480-MIB", es480tAgent=es480tAgent, es480tSystem=es480tSystem, switches=switches, es480t=es480t, sysProducts=sysProducts, intel=intel, mib2ext=mib2ext)
