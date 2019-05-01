#
# PySNMP MIB module Brocade-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Brocade-REG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:36:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Bits, ModuleIdentity, Counter32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Integer32, Counter64, IpAddress, NotificationType, ObjectIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ModuleIdentity", "Counter32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Integer32", "Counter64", "IpAddress", "NotificationType", "ObjectIdentity", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcsi = MibIdentifier((1, 3, 6, 1, 4, 1, 1588))
commDev = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2))
fibrechannel = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 1))
fcSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1))
bcsiReg = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3))
bcsiModules = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1))
mibBuilder.exportSymbols("Brocade-REG-MIB", bcsi=bcsi, fcSwitch=fcSwitch, fibrechannel=fibrechannel, bcsiReg=bcsiReg, bcsiModules=bcsiModules, commDev=commDev)
