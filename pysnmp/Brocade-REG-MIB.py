#
# PySNMP MIB module Brocade-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Brocade-REG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:19:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, enterprises, Unsigned32, TimeTicks, Bits, Counter32, IpAddress, iso, Gauge32, MibIdentifier, NotificationType, ModuleIdentity, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "enterprises", "Unsigned32", "TimeTicks", "Bits", "Counter32", "IpAddress", "iso", "Gauge32", "MibIdentifier", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bcsi = MibIdentifier((1, 3, 6, 1, 4, 1, 1588))
commDev = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2))
fibrechannel = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 1))
fcSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1))
bcsiReg = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3))
bcsiModules = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1))
mibBuilder.exportSymbols("Brocade-REG-MIB", commDev=commDev, fcSwitch=fcSwitch, bcsi=bcsi, fibrechannel=fibrechannel, bcsiReg=bcsiReg, bcsiModules=bcsiModules)
