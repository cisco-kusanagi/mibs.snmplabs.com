#
# PySNMP MIB module CPQGEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQGEN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:11:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
iso, Counter64, enterprises, Counter32, Gauge32, ObjectIdentity, Unsigned32, NotificationType, NotificationType, Integer32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "enterprises", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "NotificationType", "Integer32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
compaq = MibIdentifier((1, 3, 6, 1, 4, 1, 232))
cpqGenUnreg = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 151))
cpqGenComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 151, 2))
cpqTrapVarBind = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 151, 2, 2))
cpqGenEntOIDStr = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqGenEntOIDStr.setStatus('mandatory')
cpqGenTrapID = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqGenTrapID.setStatus('mandatory')
cpqSpecTrapID = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSpecTrapID.setStatus('mandatory')
cpqGenericUnregistered = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,99999)).setObjects(("CPQGEN-MIB", "cpqGenEntOIDStr"), ("CPQGEN-MIB", "cpqGenTrapID"), ("CPQGEN-MIB", "cpqSpecTrapID"))
mibBuilder.exportSymbols("CPQGEN-MIB", cpqGenTrapID=cpqGenTrapID, compaq=compaq, cpqGenericUnregistered=cpqGenericUnregistered, cpqTrapVarBind=cpqTrapVarBind, cpqGenEntOIDStr=cpqGenEntOIDStr, cpqGenUnreg=cpqGenUnreg, cpqGenComponent=cpqGenComponent, cpqSpecTrapID=cpqSpecTrapID)
