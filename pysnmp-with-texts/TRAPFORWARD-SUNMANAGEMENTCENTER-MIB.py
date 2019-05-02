#
# PySNMP MIB module TRAPFORWARD-SUNMANAGEMENTCENTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPFORWARD-SUNMANAGEMENTCENTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, enterprises, Counter32, iso, IpAddress, ModuleIdentity, Unsigned32, Counter64, MibIdentifier, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "enterprises", "Counter32", "iso", "IpAddress", "ModuleIdentity", "Unsigned32", "Counter64", "MibIdentifier", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity")
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
mibBuilder.exportSymbols("TRAPFORWARD-SUNMANAGEMENTCENTER-MIB", jobRemover=jobRemover, prod=prod, agent=agent, base=base, jobAdder=jobAdder, trapForward=trapForward, clientRegistrar=clientRegistrar, sunsymon=sunsymon, sun=sun)
