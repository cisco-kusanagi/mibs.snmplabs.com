#
# PySNMP MIB module TRAPFORWARD-SUNMANAGEMENTCENTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPFORWARD-SUNMANAGEMENTCENTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, MibIdentifier, Integer32, TimeTicks, iso, Counter32, Bits, Unsigned32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "MibIdentifier", "Integer32", "TimeTicks", "iso", "Counter32", "Bits", "Unsigned32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Gauge32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
prod = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
sunsymon = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12))
agent = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2))
base = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1))
trapForward = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 4))
clientRegistrar = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 4, 1))
jobAdder = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 4, 2))
jobRemover = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 4, 3))
mibBuilder.exportSymbols("TRAPFORWARD-SUNMANAGEMENTCENTER-MIB", base=base, agent=agent, sun=sun, prod=prod, trapForward=trapForward, jobAdder=jobAdder, clientRegistrar=clientRegistrar, jobRemover=jobRemover, sunsymon=sunsymon)
