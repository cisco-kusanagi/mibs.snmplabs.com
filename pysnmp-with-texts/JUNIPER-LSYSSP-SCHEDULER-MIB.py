#
# PySNMP MIB module JUNIPER-LSYSSP-SCHEDULER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-LSYSSP-SCHEDULER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:00:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
jnxLsysSpScheduler, = mibBuilder.importSymbols("JUNIPER-LSYS-SECURITYPROFILE-MIB", "jnxLsysSpScheduler")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, ModuleIdentity, Unsigned32, Integer32, ObjectIdentity, NotificationType, iso, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "ModuleIdentity", "Unsigned32", "Integer32", "ObjectIdentity", "NotificationType", "iso", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxLsysSpSchedulerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1))
if mibBuilder.loadTexts: jnxLsysSpSchedulerMIB.setLastUpdated('201005191644Z')
if mibBuilder.loadTexts: jnxLsysSpSchedulerMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxLsysSpSchedulerMIB.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: jnxLsysSpSchedulerMIB.setDescription('This module defines the scheduler-specific MIB for Juniper Enterprise Logical-System (LSYS) security profiles. Juniper documentation is recommended as the reference. The LSYS security profile provides various static and dynamic resource management by observing resource quota limits. Security scheduler resource is the focus in this MIB. ')
jnxLsysSpSchedulerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1))
jnxLsysSpSchedulerSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2))
jnxLsysSpSchedulerTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1), )
if mibBuilder.loadTexts: jnxLsysSpSchedulerTable.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerTable.setDescription('LSYSPROFILE scheduler objects for scheduler resource consumption per LSYS.')
jnxLsysSpSchedulerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1), ).setIndexNames((1, "JUNIPER-LSYSSP-SCHEDULER-MIB", "jnxLsysSpSchedulerLsysName"))
if mibBuilder.loadTexts: jnxLsysSpSchedulerEntry.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerEntry.setDescription('An entry in scheduler resource table.')
jnxLsysSpSchedulerLsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: jnxLsysSpSchedulerLsysName.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerLsysName.setDescription('The name of the logical system for which scheduler resource information is retrieved. ')
jnxLsysSpSchedulerProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpSchedulerProfileName.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerProfileName.setDescription('The security profile name string for the LSYS.')
jnxLsysSpSchedulerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpSchedulerUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerUsage.setDescription('The current resource usage count for the LSYS.')
jnxLsysSpSchedulerReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpSchedulerReserved.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerReserved.setDescription('The reserved resource count for the LSYS.')
jnxLsysSpSchedulerMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpSchedulerMaximum.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerMaximum.setDescription('The maximum allowed resource usage count for the LSYS.')
jnxLsysSpSchedulerUsedAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpSchedulerUsedAmount.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerUsedAmount.setDescription('The scheduler resource consumption over all LSYS.')
jnxLsysSpSchedulerMaxQuota = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpSchedulerMaxQuota.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerMaxQuota.setDescription('The scheduler resource maximum quota for the whole device for all LSYS.')
jnxLsysSpSchedulerAvailableAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpSchedulerAvailableAmount.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerAvailableAmount.setDescription('The scheduler resource available in the whole device.')
jnxLsysSpSchedulerHeaviestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpSchedulerHeaviestUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerHeaviestUsage.setDescription('The most amount of scheduler resource consumed of a LSYS.')
jnxLsysSpSchedulerHeaviestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpSchedulerHeaviestUser.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerHeaviestUser.setDescription('The LSYS name that consume the most scheduler resource.')
jnxLsysSpSchedulerLightestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpSchedulerLightestUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerLightestUsage.setDescription('The least amount of scheduler resource consumed of a LSYS.')
jnxLsysSpSchedulerLightestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpSchedulerLightestUser.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpSchedulerLightestUser.setDescription('The LSYS name that consume the least scheduler resource.')
mibBuilder.exportSymbols("JUNIPER-LSYSSP-SCHEDULER-MIB", jnxLsysSpSchedulerTable=jnxLsysSpSchedulerTable, jnxLsysSpSchedulerUsedAmount=jnxLsysSpSchedulerUsedAmount, jnxLsysSpSchedulerMIB=jnxLsysSpSchedulerMIB, jnxLsysSpSchedulerProfileName=jnxLsysSpSchedulerProfileName, jnxLsysSpSchedulerMaximum=jnxLsysSpSchedulerMaximum, jnxLsysSpSchedulerLsysName=jnxLsysSpSchedulerLsysName, jnxLsysSpSchedulerReserved=jnxLsysSpSchedulerReserved, PYSNMP_MODULE_ID=jnxLsysSpSchedulerMIB, jnxLsysSpSchedulerLightestUser=jnxLsysSpSchedulerLightestUser, jnxLsysSpSchedulerHeaviestUser=jnxLsysSpSchedulerHeaviestUser, jnxLsysSpSchedulerObjects=jnxLsysSpSchedulerObjects, jnxLsysSpSchedulerEntry=jnxLsysSpSchedulerEntry, jnxLsysSpSchedulerUsage=jnxLsysSpSchedulerUsage, jnxLsysSpSchedulerHeaviestUsage=jnxLsysSpSchedulerHeaviestUsage, jnxLsysSpSchedulerAvailableAmount=jnxLsysSpSchedulerAvailableAmount, jnxLsysSpSchedulerLightestUsage=jnxLsysSpSchedulerLightestUsage, jnxLsysSpSchedulerSummary=jnxLsysSpSchedulerSummary, jnxLsysSpSchedulerMaxQuota=jnxLsysSpSchedulerMaxQuota)
