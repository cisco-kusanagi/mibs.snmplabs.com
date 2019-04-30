#
# PySNMP MIB module INTEL-ES480-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-ES480-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:42:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ifPhysAddress, = mibBuilder.importSymbols("IF-MIB", "ifPhysAddress")
intel, = mibBuilder.importSymbols("INTEL-ES480-MIB", "intel")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, sysDescr = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime", "sysDescr")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Integer32, ObjectIdentity, NotificationType, NotificationType, IpAddress, MibIdentifier, Unsigned32, ModuleIdentity, Counter32, Counter64, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Integer32", "ObjectIdentity", "NotificationType", "NotificationType", "IpAddress", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Counter32", "Counter64", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
overheat = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
fanfailed = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,2)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
fanOK = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,3)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
invalidLoginAttempt = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,4)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
powerSupplyFail = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,5)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
powerSupplyGood = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,6)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
mibBuilder.exportSymbols("INTEL-ES480-TRAP-MIB", fanOK=fanOK, powerSupplyFail=powerSupplyFail, overheat=overheat, powerSupplyGood=powerSupplyGood, fanfailed=fanfailed, invalidLoginAttempt=invalidLoginAttempt)
