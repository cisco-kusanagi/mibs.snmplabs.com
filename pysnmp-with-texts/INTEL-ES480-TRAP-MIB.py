#
# PySNMP MIB module INTEL-ES480-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-ES480-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:54:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ifPhysAddress, = mibBuilder.importSymbols("IF-MIB", "ifPhysAddress")
intel, = mibBuilder.importSymbols("INTEL-ES480-MIB", "intel")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, sysDescr = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime", "sysDescr")
ModuleIdentity, Counter32, TimeTicks, Gauge32, ObjectIdentity, IpAddress, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, NotificationType, Unsigned32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "TimeTicks", "Gauge32", "ObjectIdentity", "IpAddress", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "NotificationType", "Unsigned32", "NotificationType", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
overheat = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: overheat.setDescription('A overheat trap indicates that the on board tempature sensor has reported a overheat condition. System will shutdown until unit has sufficiently cooled such that operation may begin again. A cold start trap will be issued when the unit has come back on line.')
fanfailed = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,2)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: fanfailed.setDescription('A fan failed trap indicates one or more of the cooling fans inside the device has failed. A fanOK trap will be sent once the fan has attained normal operation.')
fanOK = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,3)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: fanOK.setDescription('A fan has transitioned out of a failure state and is now operating correctly.')
invalidLoginAttempt = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,4)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: invalidLoginAttempt.setDescription('A user attempted to login to console or by telnet but was refused access due to incorrect username or password')
powerSupplyFail = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,5)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: powerSupplyFail.setDescription('One or more sources of power to this agent has failed. Presumably a redundant power-supply has taken over.')
powerSupplyGood = NotificationType((1, 3, 6, 1, 4, 1, 343) + (0,6)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: powerSupplyGood.setDescription('One or more previously bad sources of power to this agent has come back to life without causing an agent restart.')
mibBuilder.exportSymbols("INTEL-ES480-TRAP-MIB", powerSupplyFail=powerSupplyFail, overheat=overheat, fanOK=fanOK, invalidLoginAttempt=invalidLoginAttempt, powerSupplyGood=powerSupplyGood, fanfailed=fanfailed)
